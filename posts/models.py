from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class Post(models.Model):
    image = models.ImageField()
    description = models.TextField(max_length=140, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=140)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #related_name='posts'
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class UserProfile(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    # city = models.CharField(max_length=100, default='')
    # website = models.URLField(default='')
    # phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)

    # london = UserProfileManager()

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.png', upload_to='profile_pics')
#     profile_caption = models.CharField(max_length=255)

#     def __str__(self):
#         return f'{self.user.username} Profile'

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

#         image = models.open(self.image.path)
#         if image.height > 300 or image.width > 300:
#             output_size = (300, 300)
#             image.thumbnail(output_size)
#             image.save(self.image.path)
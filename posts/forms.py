from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

class EditProfileForm(UserChangeForm):
    template_name='/accounts/profile.html'
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name'
            # 'password'
        )

class Profile(DetailView):
    template_name='/accounts/profile.html'
    queryset = User.objects.all()
    def get_object(self):
        id_ = self.kwargs.get("username")
        user = get_object_or_404(User, username=id_)
        return user

    #  def get_context_data(self, *args, **kwargs):
    #     context = super(Profile,self).get_context_data(*args, **kwargs)
    #     user = self.get_object()
    #     context.update({
    #     'posts' :          user.posts.all().filter(created_date__lte=timezone.now()).order_by(' -created_date')})
    #     return context

    
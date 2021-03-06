# from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django import forms
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.forms import UserChangeForm
from django.views import generic
from .forms import EditProfileForm

from posts.models import Post, Comment

from django.contrib.auth import logout
# Create your views here.


class PostList(ListView):
    model = Post

class PostCreate(CreateView):
    model = Post
    fields = ['image', 'description', 'author']
    success_url = '/'

class CommentForm(forms.Form):
    comment = forms.CharField()

class PostDetail(DetailView):
    model = Post 

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['comment_form'] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment(
                author=request.user,
                post=self.get_object(),
                text=comment_form.cleaned_data['comment']
            )
            comment.save()
        else:
            raise Exception
        return redirect(reverse('detail', args=[self.get_object().id]))

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'accounts/profile.html'
    success_url = '/'

    def get_object(self):
        return self.request.user


def logout_view(request):
    logout(request)
    return redirect('/accounts/login')
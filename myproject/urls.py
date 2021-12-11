"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts.views import PostList, PostCreate, PostDetail, UserEditView
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile', UserEditView.as_view(template_name='posts/profile.html'), name='profile'),
    # path('accounts/profile/', include('allauth.urls')),
    # path('password/', auth_views.PasswordChangeView.as_view()),
    path('', PostList.as_view(), name='list'),
    path('new/', PostCreate.as_view(), name='new'),
    path('posts/<pk>/', PostDetail.as_view(), name='detail'),
    # path('logout', logout, name='logout'),
    path('logout', LogoutView.as_view(next_page = settings.LOGOUT_REDIRECT_URL), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# http://127.0.0.1:8000/accounts/email/

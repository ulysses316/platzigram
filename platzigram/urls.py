"""platzigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from platzigram import views as local_views
from posts import views as posts_views
from users import views as users_views
urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("hello-world/", local_views.hello, name="hello"),
    path("hola",local_views.hola, name="hola"),
    path("",local_views.index, name="index"),
    path("sorted",local_views.getPrueba1, name="sorted"),
    path("<str:name>/<int:age>", local_views.say_hi, name="get"),
    #Posts
    path("posts", posts_views.lists_posts, name="posts"),
    #users
    path("login", users_views.login_user, name="login")
]

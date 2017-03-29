"""Tweenstagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib.auth.models import User
from django.views.generic import DetailView

from feed import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^user/(?P<username>\w+)', views.ListTweetView.as_view(), name="list_tweets"),
    url(r'^cite$', views.cite, name="cite"),
    url(r'^retweet$', views.retweet, name="retweet"),
    url(r'^dummy$', views.DummyView.as_view()),
    url(r'^profile$', views.ProfileView.as_view()),
    url(r'^profile/(?P<pk>\d+)$', views.Profile2View.as_view()),
    url(r'^posts$', views.ListPosts.as_view(), name="list_posts"),
    url(r'^posts/new$', views.NewPostView.as_view()),
    url(r'^settings$', views.settings, name="settings"),

]

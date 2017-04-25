from django.contrib import admin

# Register your models here.
from feed.models import Retweet, Tweet, DummyUser, Post, Like

admin.site.register(Tweet)
admin.site.register(Retweet)
admin.site.register(Like)
admin.site.register(DummyUser)
admin.site.register(Post)
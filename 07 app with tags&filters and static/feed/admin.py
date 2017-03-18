from django.contrib import admin

# Register your models here.
from feed.models import Retweet, Tweet, DummyUser

admin.site.register(Tweet)
admin.site.register(Retweet)
admin.site.register(DummyUser)
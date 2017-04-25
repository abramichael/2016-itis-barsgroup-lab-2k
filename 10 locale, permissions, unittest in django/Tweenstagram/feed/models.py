from __future__ import unicode_literals

import datetime
import os

from django.contrib.auth.models import User
from django.db import models


class Like(models.Model):
    LIKE_TYPE = (
        ("L", "Like"),
        ("D", "Dislike"),
        ("S", "I think the same way")
    )
    user = models.ForeignKey(User),
    tweet = models.ForeignKey("Tweet")
    date = models.DateTimeField(default=datetime.datetime.today)
    like_type = models.CharField(max_length=1, choices=LIKE_TYPE)


class GeneralTweet(models.Model):
    class Meta:
        abstract = True
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=datetime.datetime.today)


class Retweet(GeneralTweet):
    tweet = models.ForeignKey("Tweet")
    def isRT(self):
        return True


def user_folder(instance, filename):
    return os.path.join(instance.user.username, filename)

class Tweet(GeneralTweet):
    class Meta:
        db_table = "tweets"
    text = models.TextField()
    image = models.ImageField(upload_to=user_folder, blank=True)
    def isRT(self):
        return False

class DummyUser(models.Model):
    username = models.CharField(max_length=20)
    followers = models.ManyToManyField("self")

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.today)

class DummyModel(models.Model):
    class Meta:
        permissions = [
            ('1', 'can_has_something'),
            ('2', 'can_has_something_else')
        ]

    name = models.CharField(max_length=10)
from __future__ import unicode_literals

import datetime

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


class Tweet(GeneralTweet):
    class Meta:
        db_table = "tweets"
    text = models.TextField()
    def isRT(self):
        return False

class DummyUser(models.Model):
    username = models.CharField(max_length=20)

    followers = models.ManyToManyField("self")
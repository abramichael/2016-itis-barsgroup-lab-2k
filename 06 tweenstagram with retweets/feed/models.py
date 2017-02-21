from __future__ import unicode_literals

import datetime

from django.contrib.auth.models import User
from django.db import models


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


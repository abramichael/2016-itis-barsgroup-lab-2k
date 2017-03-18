from itertools import chain
from operator import attrgetter

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from feed.models import Tweet, Retweet, DummyUser


@login_required
def home(request):
    if request.method == "POST":
        t = Tweet(text=request.POST["text"])
        t.user = request.user
        t.save()
        return HttpResponseRedirect(reverse("feed:home"))

    tweets = Tweet.objects.all()
    retweets = Retweet.objects.all()
    tweets_n_retweets = sorted(chain(tweets, retweets), key=attrgetter('pub_date'), reverse=True)

    return render(request, "feed/home.html", {"items": tweets_n_retweets,
                                              "s": "<a href='#'>1234</a>"})


def list_tweets(request, username):
    # tweets = Tweet.objects.filter(user__username=username).order_by("-pub_date")

    tweets = User.objects.get(username=username).tweet_set.order_by("-pub_date")
    return render(request, "feed/list_tweets.html", {"tweets": tweets})


@login_required
def cite(request):
    if request.method != "POST":
        return HttpResponse("Not supported")
    t = Tweet(user=request.user)
    origin = Tweet.objects.get(id=request.POST["tweet_id"])
    t.text = 'RT @%s: "%s" on %s' % (origin.user.username,
                                     origin.text,
                                     origin.pub_date)
    t.save()
    return HttpResponseRedirect(reverse("feed:home"))


def retweet(request):
    if request.method != "POST":
        return HttpResponse("Not supported")
    rt = Retweet(
        user=request.user,
        tweet_id=request.POST["tweet_id"]
    )
    rt.save()
    return HttpResponseRedirect(reverse("feed:home"))


def dummy(request):
    return render(request, "feed/dummy01.html")

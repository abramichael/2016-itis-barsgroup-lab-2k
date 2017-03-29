from itertools import chain
from operator import attrgetter

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView

from feed.forms import PostForm, SettingsForm, TweetForm
from feed.models import Tweet, Retweet, DummyUser, Post

@login_required
def home(request):
    if request.method == "POST":

        t = Tweet(user=request.user)
        f = TweetForm(request.POST, request.FILES, instance=t)
        f.save()
        return HttpResponseRedirect(reverse("feed:home"))

    tweets = Tweet.objects.all()
    retweets = Retweet.objects.all()
    tweets_n_retweets = sorted(chain(tweets, retweets), key=attrgetter('pub_date'), reverse=True)

    return render(request, "feed/home.html", {
                        "f": TweetForm(),
                        "items": tweets_n_retweets,
                        "s": "<a href='#'>1234</a>"})


# def list_tweets(request, username):
# tweets = Tweet.objects.filter(user__username=username).order_by("-pub_date")

#    tweets = User.objects.get(username=username).tweet_set.order_by("-pub_date")
#    return render(request, "feed/list_tweets.html", {"tweets": tweets})

@method_decorator(login_required, name="dispatch")
class ListTweetView(ListView):
    context_object_name = "tweets"
    template_name = "feed/list_tweets.html"
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        setattr(self, "username", kwargs["username"])
        return super(ListTweetView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        username = getattr(self, "username")
        return User.objects.get(username=username).tweet_set.order_by("-pub_date")


@method_decorator(login_required, name="dispatch")
class AllListTweetView(ListView):
    model = Tweet
    context_object_name = "tweets"
    template_name = "feed/list_tweets.html"
    paginate_by = 5


class LoginView(TemplateView):
    template_name = "feed/login.html"


class ProfileView(TemplateView):
    template_name = "feed/profile.html"

    def get_context_data(self, **kwargs):
        # context = super(ProfileView, self).get_context_data(**kwargs)
        # context['u'] = self.request.user
        # return context
        return {"u": self.request.user}


class Profile2View(DetailView):
    template_name = "feed/profile.html"
    context_object_name = "u"
    model = User


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


class DummyView(View):
    def dispatch(self, request, *args, **kwargs):
        return HttpResponse("DUMMY!")


class ListPosts(ListView):
    template_name = "feed/posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user).order_by("-pub_date")


class NewPostView(CreateView):
    template_name = "feed/newpost.html"
    form_class = PostForm
    success_url = reverse_lazy("feed:list_posts")

    def form_valid(self, form):
        p = Post.objects.create(user=self.request.user, **form.cleaned_data)
        return HttpResponseRedirect(self.success_url)


def settings(request):
    if request.method == "POST":
        f = SettingsForm(request.POST)
        if f.is_valid():
            return HttpResponse("GOOD: " + str(f.cleaned_data))
        else:
            return render(request, "feed/settings.html", {"f": f})
    else:
        f = SettingsForm()
        #f.prefix = "settings"
        return render(request, "feed/settings.html", {"f": f})
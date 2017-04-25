from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse


class FeedTest(TestCase):

    def setUp(self):
        self.c = Client()

    def testAnonHasNoAccessTofeed(self):
        r = self.c.get(reverse("feed:home"))
        print r.request["PATH_INFO"]
        print r.url
        self.assertEquals(302, r.status_code)

    def testLoggedUserHasAccessToFeed(self):
        u = User.objects.create_user(
            username="user",
            password="user"
        )
        self.c.login(
            username="user",
            password="user"
        )
        r = self.c.get(reverse("feed:home"))
        self.assertEquals(200, r.status_code)


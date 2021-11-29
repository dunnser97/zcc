from django.test import SimpleTestCase
from django.urls import reverse, resolve
from masterOfTickets.views import home, individual_ticket, showMeLists


class TestUrls(SimpleTestCase):

    def test_home_url(self):
        url = reverse("home")
        print(url)
        self.assertEquals(resolve(url).func, home)

    def test_home_url(self):
        url = reverse("showMeLists")
        self.assertEquals(resolve(url).func, showMeLists)
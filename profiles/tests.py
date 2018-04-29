from urllib import parse

from django.test import TestCase
from django.urls import reverse

from . import factories


class LoggedInRepresentativeUpdateViewTestCase(TestCase):

    def setUp(self):
        self.obj = factories.RepresentativeFactory.create()
        self.profile_url = reverse("profile")

    def test_call_view_denies_anonymous(self):
        response = self.client.get(self.profile_url, follow=True)
        path = "{}?next={}".format(reverse("login"), parse.quote_plus(self.profile_url))
        self.assertRedirects(response, path)

    def test_call_view_loads(self):
        self.client.force_login(self.obj.user_ptr)
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile_update_form.html")

    def test_with_staff_user(self):
        user = factories.StaffUser.create()
        self.client.force_login(user)
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 403)

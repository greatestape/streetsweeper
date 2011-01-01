from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase

from photos.models import Photo
from streets.models import Street


class HomePageTestCase(TestCase):
    def setUp(self):
        self.photo = self.create_photo()

    def create_street(self):
        return Street.objects.create(name="Test Streets")

    def create_user(self):
        return User.objects.create(username='test-user')

    def create_photo(self, street=None, owner=None, x_offset=0):
        if street is None:
            street = self.create_street()
        if owner is None:
            owner = self.create_user()
        return Photo.objects.create(
                photo='no-photo.fakepg',
                width=200,
                height=200,
                street=street,
                owner=owner,
                side_of_street='side-a',
                x_offset=x_offset,
                )

    def testHomePageLoads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def testHomePageLoadsHomeTemplate(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home/home.html')

    def testPhotosAppearOnHomePage(self):
        response = self.client.get('/')
        self.assertContains(response, self.photo.photo.url)

    def testPhotosOutOfRangeNotDisplayed(self):
        # TODO
        pass

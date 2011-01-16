from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase

from photos.models import Photo
from streets.models import Street
from streets.tests import StreetHelper


class HomePageTestCase(TestCase, StreetHelper):
    def setUp(self):
        self.photo = self.create_photo()

    def create_user(self):
        return User.objects.create(username='test-user')

    def create_photo(self, owner=None, x_offset=0, filename='no-photo.fake'):
        if owner is None:
            owner = self.create_user()
        return Photo.objects.create(
                photo=filename,
                width=200,
                height=200,
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
        in_range_photo = self.create_photo(owner=self.photo.owner,
                x_offset=195, filename='in-range-photo.fake')
        out_of_range_photo = self.create_photo(owner=self.photo.owner,
                x_offset=-10, filename='out-of-range-photo.fake')
        response = self.client.get('/',
                {'position': '200', 'width': '1200', 'scale': '15'})
        self.assertEqual(response.context['centre_position'], 200,
                "Position was %s instead of %s. Query string was: %s" % (
                response.context['centre_position'],
                200,
                response.request['QUERY_STRING']))
        self.assertEqual(response.context['width_in_pixels'], 1200,
                "Width in pixels was %s instead of %s. Query string was: %s" % (
                response.context['width_in_pixels'],
                1200,
                response.request['QUERY_STRING']))
        self.assertEqual(response.context['scale'], 15,
                "Scale was %s instead of %s. Query string was: %s" % (
                response.context['scale'],
                15,
                response.request['QUERY_STRING']))
        self.assertEqual(response.context['width_in_metres'], 80,
                "Width in metres was %s instead of %s. Query string was: %s" % (
                response.context['width_in_metres'],
                80,
                response.request['QUERY_STRING']))
        self.assertTrue(in_range_photo in response.context['photo_list'],
                "%s not found in %s" % (in_range_photo, response.context['photo_list']))
        self.assertContains(response, in_range_photo.photo.url, 1, 200,
                "Couldn't find '%s' in response: %s" % (
                in_range_photo.photo.url,
                response.content))
        self.assertNotContains(response, out_of_range_photo.photo.url)

    def testOnlyStreetsInRangeAreDisplayed(self):
        in_range_street = self.create_street(x_offset=-475, name='Near Street')
        out_of_range_street = self.create_street(x_offset=-1050, name='Far Street')
        response = self.client.get('/',
                {'position': '-440', 'width': '1200', 'scale': '15'})
        self.assertTrue(in_range_street in response.context['street_list'],
                "In range street %s not found in %s" %
                (in_range_street, response.context['street_list']))
        self.assertTrue(out_of_range_street not in response.context['street_list'],
                "Out of range street %s unexpectedly found in %s" %
                (out_of_range_street, response.context['street_list']))
        self.assertContains(response, in_range_street.name)
        self.assertNotContains(response, out_of_range_street)

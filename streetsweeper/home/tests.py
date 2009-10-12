from django.test import TestCase

from mosaics.models import Mosaic


class HomePageTestCase(TestCase):
    def testHomePageLoads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def testHomePageLoadsHomeTemplate(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home/home.html')


class MosaicTestCase(TestCase):
    """Tests that the home page uses mosaics properly"""
    def testHomePageContainsMosaicCompositeImage(self):
        mosaic = Mosaic.objects.create(name='Test', slug='north')
        mosaic.slice_set.create(
                width=100,
                height=100,
                x_offset=0,
                y_offset=0
                )
        response = self.client.get('/')
        self.assertTrue(mosaic.slice_set.all()[0] in response.context['slices'])

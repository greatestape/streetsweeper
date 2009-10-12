from django.test import TestCase


class HomePageTestCase(TestCase):
    def testHomePageLoads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def testHomePageLoadsHomeTemplate(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home/home.html')

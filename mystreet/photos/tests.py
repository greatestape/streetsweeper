import os.path

import Image

from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TestCase

from photos.models import Photo

TEST_PHOTO = 'static/test_files/photo1.jpg'

class PhotoUploadTestCase(TestCase):
    """Testing that photos can be uploaded"""
    def setUp(self):
        self.upload_url = reverse('photo_upload')
        self.test_file = _get_test_photo_file()
        self.test_name = 'Cat Photo'
        self.response = self.client.post(self.upload_url, {'name': self.test_name, 'photo': open(self.test_file)})

    def testPhotoUploadRedirectsToStatusView(self):
        self.assertRedirects(self.response, reverse('photo_upload_status'))

    def testPhotoInDB(self):
        self.assertEqual(Photo.objects.count(), 1)
        new_photo = Photo.objects.all()[0]
        actual_file = open(self.test_file)
        actual_image = Image.open(self.test_file)
        actual_width, actual_height = actual_image.size
        self.assertEqual(actual_file.read(), new_photo.photo.read())
        self.assertEqual(new_photo.width, actual_width)
        self.assertEqual(new_photo.height, actual_height)

    def tearDown(self):
        Photo.objects.all()[0].delete()


def _get_test_photo_file():
    return os.path.join(settings.MEDIA_ROOT, TEST_PHOTO)

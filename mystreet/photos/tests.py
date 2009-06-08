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

    def testPhotoUploadPost(self):
        test_file = _get_test_photo_file()
        test_name = 'Cat Photo'
        response = self.client.post(self.upload_url, {'name': test_name, 'photo': open(test_file)})
        self.assertRedirects(response, reverse('photo_upload_status'))
        self.assertEqual(Photo.objects.count(), 1)
        new_photo = Photo.objects.all()[0]
        actual_file = open(test_file)
        actual_image = Image.open(test_file)
        actual_width, actual_height = actual_image.size
        self.assertEqual(actual_file.read(), new_photo.photo.read())
        self.assertEqual(new_photo.width, actual_width)
        self.assertEqual(new_photo.height, actual_height)

    def testPhotoUploadGet(self):
        response = self.client.get(self.upload_url)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        for photo in Photo.objects.all():
            photo.delete()


def _get_test_photo_file():
    return os.path.join(settings.MEDIA_ROOT, TEST_PHOTO)

import os.path

import Image

from django.conf import settings
from django.contrib.auth.models import User
from django.core.files import File
from django.core.urlresolvers import reverse
from django.test import TestCase

from photos.models import Photo
from streets.models import Street

TEST_PHOTO = 'static/test_files/photo1.jpg'

class PhotoUploadTestCase(TestCase):
    """Testing that photos can be uploaded"""
    def setUp(self):
        self.upload_url = reverse('photo_upload')
        self.user = User.objects.create_user('testuser', 'testuser@test.com', 'testpw')

    def testPhotoUploadPost(self):
        test_file = _get_media_file_path(TEST_PHOTO)
        self.client.login(username='testuser', password='testpw')
        response = self.client.post(self.upload_url, {'photo': open(test_file)})
        self.assertEqual(Photo.objects.count(), 1)
        new_photo = Photo.objects.all()[0]
        self.assertRedirects(response, new_photo.get_absolute_url())
        actual_file = open(test_file)
        actual_image = Image.open(test_file)
        actual_width, actual_height = actual_image.size
        self.assertEqual(actual_file.read(), new_photo.photo.read())
        self.assertEqual(new_photo.width, actual_width)
        self.assertEqual(new_photo.height, actual_height)
        self.assertEqual(new_photo.owner, self.user)

    def testPhotoUploadGet(self):
        self.client.login(username='testuser', password='testpw')
        response = self.client.get(self.upload_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/upload.html')

    def testNoFileError(self):
        self.client.login(username='testuser', password='testpw')
        response = self.client.post(self.upload_url)
        self.assertFormError(response, 'form', 'photo', 'Please provide a photo for upload.')

    def testUnauthenticatedGetRedirects(self):
        response = self.client.get(self.upload_url)
        self.assertRedirects(response, '%s?next=%s' % (settings.LOGIN_URL, self.upload_url))

    def tearDown(self):
        for photo in Photo.objects.all():
            photo.delete()


class PhotoStatusTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'testuser@test.com', 'testpw')
        self.street = self.create_street()
        self.photo = Photo.objects.create(owner=self.user, street=self.street)
        self.photo.photo = _get_media_file_path(TEST_PHOTO)
        self.photo.save()

    def create_street(self):
        return Street.objects.create(name="Test Streets")

    def testStatusPage(self):
        response = self.client.get(self.photo.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/photo_detail.html')


def _get_media_file_path(path):
    return os.path.join(settings.MEDIA_ROOT, path)

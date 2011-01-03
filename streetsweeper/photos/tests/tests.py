import os.path

import Image

from django.conf import settings
from django.contrib.auth.models import User
from django.core.files import File
from django.core.urlresolvers import reverse
from django.test import TestCase

from photos.models import Photo
from streets.models import Street

TEST_PHOTO = os.path.join(
        os.path.realpath(os.path.dirname(__file__)),
        'photo1.jpg')


class PhotoTestCase(TestCase):
    def setUp(self):
        super(PhotoTestCase, self).setUp()
        self.upload_url = reverse('photo_upload')
        self.street = self.create_street()
        self.user = User.objects.create_user('testuser', 'testuser@test.com', 'testpw')
        self.client.login(username='testuser', password='testpw')
        self.photos_to_delete = []

    def tearDown(self):
        for photo in self.photos_to_delete:
            photo.delete()

    def create_street(self):
        return Street.objects.create(name="Test Street")

    def create_photo(self):
        old_photo_count = Photo.objects.count()
        response = self.client.post(reverse('photo_upload'), {
                'photo': open(TEST_PHOTO), 'x_offset': '0'})
        if response.context and 'form' in response.context:
            form_errors = response.context['form'].errors
        else:
            form_errors = None
        self.assertEqual(Photo.objects.count(), old_photo_count + 1,
                "Photo wasn't created." +
                (" Form errors: %s" % form_errors.as_text() if form_errors else ''))
        photo = Photo.objects.latest('id')
        self.photos_to_delete.append(photo)
        return photo


class PhotoUploadTests(PhotoTestCase):
    """Testing that photos can be uploaded"""
    def testPhotoUploadPost(self):
        response = self.client.post(self.upload_url, {
                'photo': open(TEST_PHOTO), 'x_offset': '0'})
        self.assertEqual(Photo.objects.count(), 1)
        new_photo = Photo.objects.all()[0]
        self.assertRedirects(response, new_photo.get_absolute_url())
        actual_file = open(TEST_PHOTO)
        actual_image = Image.open(TEST_PHOTO)
        actual_width, actual_height = actual_image.size
        self.assertEqual(actual_file.read(), new_photo.photo.read())
        self.assertEqual(new_photo.width, actual_width)
        self.assertEqual(new_photo.height, actual_height)
        self.assertEqual(new_photo.owner, self.user)

    def testPhotoUploadGet(self):
        response = self.client.get(self.upload_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/upload.html')

    def testNoFileError(self):
        response = self.client.post(self.upload_url)
        self.assertFormError(response, 'form', 'photo', 'Please provide a photo for upload.')

    def testUnauthenticatedGetRedirects(self):
        self.client.logout()
        response = self.client.get(self.upload_url)
        self.assertRedirects(response, '%s?next=%s' % (settings.LOGIN_URL, self.upload_url))

    def tearDown(self):
        for photo in Photo.objects.all():
            photo.delete()


class PhotoStatusTests(PhotoTestCase):
    def testStatusPage(self):
        photo = self.create_photo()
        response = self.client.get(photo.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/photo_detail.html')

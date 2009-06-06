from django.conf.urls.defaults import *
from django.contrib import admin


urlpatterns = patterns('photos.views',
    (r'^upload/$', 'upload', {}, 'photo_upload'),
    (r'^upload/success/$', 'success', {}, 'photo_upload_status'),
)

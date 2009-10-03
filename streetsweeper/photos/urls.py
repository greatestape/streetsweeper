from django.conf.urls.defaults import *
from django.contrib import admin


urlpatterns = patterns('photos.views',
    (r'^upload/$', 'upload', {}, 'photo_upload'),
    (r'^detail/(?P<id>\d+)/$', 'detail', {}, 'photo_detail'),
)

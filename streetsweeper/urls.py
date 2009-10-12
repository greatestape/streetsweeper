from django.conf.urls.defaults import *
from django.contrib import admin


urlpatterns = patterns('',
    (r'^$', 'home.views.home', {}, 'home'),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),
    (r'^photos/', include('photos.urls')),
    (r'^accounts/', include('django.contrib.auth.urls')),
)

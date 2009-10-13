from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    (r'^$', 'home.views.home', {}, 'home'),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^photos/', include('photos.urls')),
    (r'^accounts/', include('django.contrib.auth.urls')),
)

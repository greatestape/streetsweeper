from django.conf import settings
from django.views.generic import simple

from photos.models import Photo


def home(request):
    photos = Photo.objects.all()
    return simple.direct_to_template(
            request,
            'home/home.html',
            {'photo_list': photos},
            )

from django.conf import settings
from django.views.generic import simple

from mosaics.models import Mosaic


def home(request):
    mosaic = Mosaic.objects.get_by_slug(settings.DEFAULT_MOSAIC)
    return simple.direct_to_template(
            request,
            'home/home.html',
            {'mosaic': mosaic},
            )

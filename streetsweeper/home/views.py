from django.conf import settings
from django.views.generic import simple

from mosaics.models import Mosaic


def home(request):
    mosaic = Mosaic.objects.get_by_slug(settings.DEFAULT_MOSAIC)
    slices = mosaic.slice_set.get_for_x_range(0, settings.HOME_MOSAIC_PIXEL_WIDTH)
    return simple.direct_to_template(
            request,
            'home/home.html',
            {'mosaic': mosaic,
            'slices': slices
            })

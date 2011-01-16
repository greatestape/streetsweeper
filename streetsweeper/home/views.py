from django.conf import settings
from django.http import HttpResponseBadRequest
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.generic import simple

from photos.models import Photo

from home.forms import ViewportForm


def home(request):
    form = ViewportForm(request.GET)
    if not form.is_valid():
        return HttpResponseBadRequest(render_to_string(
                '400.html',
                {'errors': form.errors},
                RequestContext(request)))
    # TODO: Treat width as a value in pixels, add "scale" field
    # for determining the extent of the street that should be displayed
    width = form.cleaned_data['width']
    position = form.cleaned_data['position']
    photos = Photo.objects.filter(
            x_offset__gte=position - width / 2.0,
            x_offset__lte=position + width / 2.0,
            )
    return simple.direct_to_template(
            request,
            'home/home.html',
            {'photo_list': photos,
            'position': position,
            'width': width,
            },)

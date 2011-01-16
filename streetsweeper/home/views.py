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
    width_in_pixels = form.cleaned_data['width']
    position = form.cleaned_data['position']
    scale = form.cleaned_data['scale']
    width_in_metres = width_in_pixels / scale
    left_edge = position - width_in_metres / 2.0
    right_edge = position + width_in_metres / 2.0
    photos = Photo.objects.filter(
            x_offset__gte=left_edge,
            x_offset__lte=right_edge,
            )
    return simple.direct_to_template(
            request,
            'home/home.html',
            {'photo_list': photos,
            'centre_position': position,
            'left_edge': left_edge,
            'right_edge': right_edge,
            'width_in_pixels': width_in_pixels,
            'width_in_metres': width_in_metres,
            'scale': scale,
            },)

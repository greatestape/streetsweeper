from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import simple

from photos.models import Photo

def upload(request):
    Photo.objects.create(height=1, width=1)
    return HttpResponseRedirect(reverse('photo_upload_status'))


def success(request):
    return HttpResponse('')
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import simple

from photos.forms import UploadForm
from photos.models import Photo


def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('photo_upload_status'))
    else:
        form = UploadForm()
    return simple.direct_to_template(request, 'photos/upload.html', {'form': form})


def success(request):
    return HttpResponse('')
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import simple, list_detail

from photos.forms import UploadForm
from photos.models import Photo


@login_required
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            return HttpResponseRedirect(photo.get_absolute_url())
    else:
        form = UploadForm()
    return simple.direct_to_template(request, 'photos/upload.html', {'form': form})


def detail(request, id):
    return list_detail.object_detail(
            request,
            Photo.objects.all(),
            id,
            template_object_name='photo'
            )

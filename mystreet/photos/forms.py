from django import forms
from django.utils.translation import ugettext_lazy as _

from photos.models import Photo


class UploadForm(forms.ModelForm):
    photo = forms.ImageField(error_messages={'required': 'Please provide a photo for upload.'})

    class Meta:
        model = Photo
        fields = ('photo',)

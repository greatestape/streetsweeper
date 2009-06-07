from django import forms

from photos.models import Photo


class UploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photo',)

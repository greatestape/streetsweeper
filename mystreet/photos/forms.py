from django import forms

from photos.models import Photo


class UploadForm(forms.ModelForm):
    photo = forms.ImageField(error_messages={'required': 'Please provide a photo for upload.'})

    class Meta:
        model = Photo
        fields = ('photo',)

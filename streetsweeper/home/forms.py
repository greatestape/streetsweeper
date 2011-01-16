from django import forms

DEFAULT_WIDTH = 100
DEFAULT_POSITION = 0.0


class ViewportForm(forms.Form):
    position = forms.FloatField(required=False)
    width = forms.IntegerField(required=False)

    def clean_width(self):
        width = self.cleaned_data.get('width')
        return width or DEFAULT_WIDTH

    def clean_position(self):
        width = self.cleaned_data.get('position')
        return width or DEFAULT_POSITION

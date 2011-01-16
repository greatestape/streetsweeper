from django import forms
from django.utils.translation import ugettext as _

DEFAULT_WIDTH = 1000
DEFAULT_POSITION = 0.0
DEFAULT_SCALE = 10.0


class ViewportForm(forms.Form):
    position = forms.FloatField(label=_('position (m)'), required=False,
            help_text=_("The position along the street upon which the "
            "viewport should be centred."))
    width = forms.IntegerField(label=_('width (px)'), required=False,
            help_text=_("The width of the viewport in pixels"))
    scale = forms.FloatField(label=_('scale (px/m)'), required=False,
            help_text=_("The scale to display the street at in the viewport"))

    def clean_width(self):
        width = self.cleaned_data.get('width')
        return width or DEFAULT_WIDTH

    def clean_position(self):
        position = self.cleaned_data.get('position')
        return position or DEFAULT_POSITION

    def clean_scale(self):
        scale = self.cleaned_data.get('scale')
        return scale or DEFAULT_SCALE

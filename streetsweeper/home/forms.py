from django import forms
from django.utils.translation import ugettext as _

DEFAULT_WIDTH = 100
DEFAULT_POSITION = 0.0


class ViewportForm(forms.Form):
    position = forms.FloatField(label=_('position (m)'), required=False,
            help_text=_("The position along the street upon which the "
            "viewport should be centred."))
    width = forms.IntegerField(label=_('width (m)'), required=False,
            help_text=_("The width of the viewport in metres"))

    def clean_width(self):
        width = self.cleaned_data.get('width')
        return width or DEFAULT_WIDTH

    def clean_position(self):
        position = self.cleaned_data.get('position')
        return position or DEFAULT_POSITION

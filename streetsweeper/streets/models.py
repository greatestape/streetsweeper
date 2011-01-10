from django.db import models
from django.utils.translation import ugettext_lazy as _


class Street(models.Model):
    """A street that will be depicted using mosaics"""
    name = models.CharField(_('name'), max_length=255)
    x_offset = models.IntegerField(_('x offset'),
            help_text=_("Offset in meters from home street's origin."))
    # TODO: Add fields for setting separate names for the part of the street
    # "below" the origin and the part "above" the origin (ex. Queen St. W,
    # Queen St. E)

    class Meta:
        verbose_name = _(u'street')
        verbose_name_plural = _(u'streets')

    def __unicode__(self):
        return self.name

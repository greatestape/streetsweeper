from django.db import models
from django.utils.translation import ugettext_lazy as _


class Street(models.Model):
    """A street that will be depicted using mosaics"""
    name = models.CharField(_('name'), max_length=255)

    class Meta:
        verbose_name = _(u'street')
        verbose_name_plural = _(u'streets')

    def __unicode__(self):
        return self.name

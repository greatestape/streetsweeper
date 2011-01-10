from django.db import models
from django.utils.translation import ugettext as _, ugettext_lazy as _lazy


class Street(models.Model):
    """A street that will be depicted using mosaics"""
    name = models.CharField(_lazy('name'), max_length=255)

    class Admin:
        list_display = ('name',)
        search_fields = ('name',)

    class Meta:
        verbose_name = _(u'street')
        verbose_name_plural = _(u'streets')

    def __unicode__(self):
        return self.name

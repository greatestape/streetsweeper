from django.db import models
from django.utils.translation import ugettext as _, ugettext_lazy as _lazy

class Street(models.Model):
    """A street that will be depicted using mosaics"""
    name = models.CharField(max_length=100, _lazy('name'))

    class Admin:
        list_display = ('name',)
        search_fields = ('name',)

    class Meta:
        verbose_name = _(u'street')
        verbose_name_plural = _(u'streets')

    def __unicode__(self):
        return _(u'%(name)s') % {'name': self.name}


class Patch(models.Model):
    """A Patch is a single image element with placement and cropping information for rendering it within a mosaic"""
    name = models.CharField(blank=True, max_length=100)

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __str__(self):
        return "Patch"

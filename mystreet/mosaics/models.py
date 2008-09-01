from django.db import models
from django.utils.translation import ugettext as _, ugettext_lazy as _lazy

class Mosaic(models.Model):
    """A mosaic of images"""
    name = models.CharField(blank=True, max_length=100)

    class Admin:
        list_display = ('name',)
        search_fields = ('name',)

    class Meta:
        verbose_name = _(u'mosaic')
        verbose_name_plural = _(u'mosaics')

    def __unicode__(self):
        return _(u'%(name)') % {'name': self.name}


class Patch(models.Model):
    """A Patch is a single image element with placement and cropping information for rendering it within a mosaic"""
    mosaic = models.ForeignKey(Mosaic, verbose_name=_lazy(u'mosaic'))
    scale = models.FloatField(_lazy('scale'), help_text=_lazy('The number of pixels in one AU (arbitrary unit) in the mosaic'))
    position_x = models.FloatField(_lazy('position (x)'))
    position_y = models.FloatField(_lazy('position (y)'))
    
    source_image = models.ForeignKey('Photo', verbose_name=_lazy(u'source image'))
    colour_correction = models.ForeignKey('ColourCorrection', verbose_name=_lazy(u'colour correction'))
    rotation = models.FloatField(_lazy('rotation'), help_text=_lazy('measured in radians, positive values rotate counte-clockwise'))
    cropping = models.

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __str__(self):
        return "Patch"

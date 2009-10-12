from django.db import models
from django.utils.translation import ugettext as _, ugettext_lazy as _lazy


class Mosaic(models.Model):
    """A mosaic of images"""
    name = models.CharField(_('name'), blank=True, max_length=255)
    slug = models.SlugField(_('slug'), unique=True)

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
    rotation = models.FloatField(_lazy('rotation'), help_text=_lazy('measured in radians, positive values rotate counte-clockwise'))
    mask = models.CommaSeparatedIntegerField(_('mask'), blank=True, max_length=512)
    modified_image = models.ImageField(_('modified image'), upload_to='managed/patch_caches', null=True, blank=True,)

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __str__(self):
        return "Patch"


def get_modified_file_path(instance, filename):
    return 'files/mosaics/%s/patches/%s/%s' % (
        getattr(getattr(instance,'mosaic',None),'slug','unknown'),
        getattr(instance,'pk','unknown'),
        filename)
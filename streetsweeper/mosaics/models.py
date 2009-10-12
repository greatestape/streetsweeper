from django.db import models
from django.utils.translation import ugettext_lazy as _

from mega_manager import make_manager

from mosaics.managers import MosaicManager, TileManager


class Mosaic(models.Model):
    """A mosaic of images"""
    name = models.CharField(_('name'), blank=True, max_length=255)
    slug = models.SlugField(_('slug'), unique=True)

    objects = MosaicManager()

    class Admin:
        list_display = ('name',)
        search_fields = ('name',)

    class Meta:
        verbose_name = _(u'mosaic')
        verbose_name_plural = _(u'mosaics')

    def __unicode__(self):
        return _(u'%(name)s') % {'name': self.name}


class Slice(models.Model):
    """A pre-rendered tile of a mosaic"""
    mosaic = models.ForeignKey(Mosaic, verbose_name=_("mosaic"))
    width = models.IntegerField(_('the width of the tile'))
    height = models.IntegerField(_('the height of the tile'))
    x_offset = models.IntegerField(_('the offset on x from the mosaic origin (in pixel-space)'))
    y_offset = models.IntegerField(_('the offset on y from the mosaic origin (in pixel-space)'))
    image = models.ImageField(upload_to="managed/tiles", height_field=height, width_field=width)

    objects = make_manager(TileManager)

    class Meta:
        verbose_name = _("Tile")
        verbose_name_plural = _("Tiles")

    def __unicode__(self):
        return u"Tile %d in mosaic %s" % (self.pk, self.mosaic)


class Patch(models.Model):
    """A Patch is a single image element with placement and cropping information for rendering it within a mosaic"""
    mosaic = models.ForeignKey(Mosaic, verbose_name=_(u'mosaic'))
    scale = models.FloatField(_('scale'), help_text=_('The number of pixels in one AU (arbitrary unit) in the mosaic'))
    position_x = models.FloatField(_('position (x)'))
    position_y = models.FloatField(_('position (y)'))

    source_image = models.ForeignKey('photos.Photo', verbose_name=_(u'source image'))
    rotation = models.FloatField(_('rotation'), help_text=_('measured in radians, positive values rotate counte-clockwise'))
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
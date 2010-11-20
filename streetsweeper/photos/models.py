from django.db import models
from django.utils.translation import ugettext_lazy as _

from streets.choices import STREET_SIDE_CHOICES


class Photo(models.Model):
    """An uploaded photo"""
    owner = models.ForeignKey('auth.User', verbose_name=_("owner"))
    photo = models.ImageField(upload_to="managed/photos", height_field='height', width_field='width')
    width = models.IntegerField(_('width'), null=True, blank=True)
    height = models.IntegerField(_('height'), null=True, blank=True)
    street = models.ForeignKey('streets.Street', verbose_name=_('street'))
    side_of_street = models.CharField(_('side of street'), max_length=255,
            choices=STREET_SIDE_CHOICES)

    class Meta:
        verbose_name = _("Photo")
        verbose_name_plural = _("Photos")

    def __unicode__(self):
        return self.photo.name

    @models.permalink
    def get_absolute_url(self):
        return ('photo_detail', (), {'id': self.id})

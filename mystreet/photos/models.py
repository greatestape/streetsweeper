from django.db import models
from django.utils.translation import ugettext_lazy as _


class Photo(models.Model):
    """An uploaded photo"""
    height = models.IntegerField(_('height'))
    width = models.IntegerField(_('width'))
    photo = models.ImageField(upload_to="managed/photos", height_field=height, width_field=width)

    class Meta:
        verbose_name = _("Photo")
        verbose_name_plural = _("Photos")

    def __unicode__(self):
        return self.photo.name

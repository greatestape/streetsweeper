from django.db import models
from django.utils.translation import ugettext as _, ugettext_lazy as _lazy

class Street(models.Model):
    """A street that will be depicted using mosaics"""
    name = models.CharField(_lazy('name'), max_length=100)
    sides = models.ManyToManyField(StreetSides, verbose_name=_lazy(u'sides'))

    class Admin:
        list_display = ('name',)
        search_fields = ('name',)

    class Meta:
        verbose_name = _(u'street')
        verbose_name_plural = _(u'streets')

    def __unicode__(self):
        return _(u'%(name)s') % {'name': self.name}

class AddressedLocation(models.Model):
    """An addressed place on a street"""
    address = AddressField(_lazy('address'))
    offset = models.PositiveIntegerField(_lazy('offset'), help_text=_lazy('offset from street origin measured in metres'))
    length = models.PositiveIntegerField(_lazy('length'), help_text=_lazy('length of this address in terms of "street-front real estate", measured in metres'))

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    class Meta:
        verbose_name = _(u'')

    def __unicode__(self):
        return u'Address'


class Block(models.Model):
    """A block of a city street"""
    street = models.ForeignKey(Street, verbose_name=_lazy(u'street'))
    side = models.CharField(_lazy('side of street'), choices=STREET_SIDE_CHOICES)
    begin_address = models.ForeignKey(AddressedLocation, verbose_name=_lazy(u'begin address'), to_field='address', blank=True, null=True, related_name='blocks_begun_here')
    end_address = models.ForeignKey(AddressedLocation, verbose_name=_lazy(u'end address'), to_field='address', blank=True, null=True, related_name='blocks_ending_here')

    def get_side_street_combo(self):
        return _(u'%(side_initials)s side of %(street)s') % {'side_initials': self.side.initials, 'street': self.street.name}


    class Admin:
        list_display = ('get_side_street_combo', )
        search_fields = ('',)

    class Meta:
        verbose_name = _(u'')

    def __unicode__(self):
        return u'Block'


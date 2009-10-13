from django.contrib import admin

from mosaics.models import Mosaic, Slice, Patch


class MosaicAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class SliceAdmin(admin.ModelAdmin):
    list_display = ('mosaic', 'x_offset', 'y_offset', 'width', 'height', 'image')
    list_filter = ('mosaic',)


class PatchAdmin(admin.ModelAdmin):
    list_display = ('mosaic', 'scale', 'position_x', 'position_y', 'source_image',)
    list_filter = ('mosaic',)


admin.site.register(Mosaic, MosaicAdmin)
admin.site.register(Slice, SliceAdmin)
admin.site.register(Patch, PatchAdmin)

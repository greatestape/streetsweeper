from django.contrib import admin

from photos.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'side_of_street', 'x_offset', 'width', 'height')


admin.site.register(Photo, PhotoAdmin)

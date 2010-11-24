from django.contrib import admin

from photos.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'street', 'side_of_street')


admin.site.register(Photo, PhotoAdmin)

from django.contrib import admin

from streets.models import Street


class StreetAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Street, StreetAdmin)

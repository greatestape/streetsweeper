from django.db import models

class Patch(models.Model):
    """A Patch is a single image element with placement and cropping information for rendering it within a mosaic"""
    name = models.CharField(blank=True, max_length=100)

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __str__(self):
        return "Patch"

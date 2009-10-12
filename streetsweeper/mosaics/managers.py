from django.db import models


class MosaicManager(models.Manager):
    mosaic_cache = {}

    def get_by_slug(self, slug):
        return self.mosaic_cache.setdefault(slug, self.get_query_set().get(slug=slug))


class TileQuerySet(models.query.QuerySet):
    def get_for_x_range(self, x_min, x_max):
        return self.filter(
                x_offset__gte=x_min - models.F('width'),
                x_offset__lte=x_max
                )


class TileManager(models.Manager):
    use_for_related_fields = True

    query_set_class = TileQuerySet

    def get_for_x_range(self, x_min, x_max):
        return self.get_query_set().get_for_x_range(x_min, x_max)

from django.db import models

from mega_manager import make_manager


BLUE = 'blue'
RED = 'red'
FRISBEE_COLOURS = [
    (BLUE, 'Blue'),
    (RED, 'Red')
    ]


class FancyQuerySet(models.query.QuerySet):
    def fancy(self):
        return self.filter(fancy=True)


class FancyManager(models.Manager):
    query_set_class = FancyQuerySet

    def fancy(self):
        return self.get_query_set().filter(fancy=True)


class ColourQuerySet(models.query.QuerySet):
    def blue(self):
        return self.filter(colour=BLUE)


class ColourManager(models.Manager):
    query_set_class = ColourQuerySet

    def blue(self):
        return self.get_query_set().filter(colour=BLUE)


class SportsLocker(models.Model):
    owner = models.CharField(null=False, max_length=255)


class Frisbee(models.Model):
    """A simple frisbee"""
    colour = models.CharField(choices=FRISBEE_COLOURS, null=False, max_length=255)
    fancy = models.BooleanField(default=True)
    sports_locker = models.ForeignKey(SportsLocker)

    objects = make_manager(FancyManager, ColourManager)

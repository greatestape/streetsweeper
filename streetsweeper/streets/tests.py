from streets.models import Street


class StreetHelper(object):
    def create_street(self, x_offset=0):
        return Street.objects.create(name="Test Street", x_offset=x_offset)

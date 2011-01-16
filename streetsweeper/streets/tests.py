from streets.models import Street


class StreetHelper(object):
    def create_street(self, x_offset=0, name='Test Street'):
        return Street.objects.create(name=name, x_offset=x_offset)

from streets.models import Street


class StreetHelper(object):
    def create_street(self):
        return Street.objects.create(name="Test Street")

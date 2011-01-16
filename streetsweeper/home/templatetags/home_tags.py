from django import template

register = template.Library()


@register.filter
def format_distance(distance):
    if distance > 0:
        return '{0:n} m east'.format(distance)
    else:
        return '{0:n} m west'.format(abs(distance))

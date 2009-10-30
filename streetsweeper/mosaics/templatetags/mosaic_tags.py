import Image
import os.path

from django.conf import settings
from django import template


register = template.Library()


@register.inclusion_tag('mosaics/includes/mosaic.html')
def show_mosaic(mosaic, width, height, zoom, edge_height, xoffset):
    file_path = (
            'managed/mosaics/%(mosaic)s/'
            '%(width)sx%(height)sx%(zoom)s-eh%(edge_height)s/'
            'xoffset%(xoffset)s.jpg' % {
                'mosaic': mosaic.slug,
                'width': width,
                'height': height,
                'zoom': zoom,
                'edge_height': edge_height,
                'xoffset': xoffset
            }
            )

    local_file_path = os.path.join(
        settings.MEDIA_ROOT,
        file_path
        )
    if(not os.path.exists(local_file_path)):
        os.makedirs(os.path.dirname(local_file_path))

        image = Image.new('RGBA', (width, height))
        image.save(local_file_path)

    # TODO: gather tiles required to render area of mosaic defined by parameters
    # Open each tile and place it in the PIL image at the appropriate coordinates
    # Save the image to the generated filename
    # return the filename (to the template, which should generate the image tag)
    return {'slice_url': '%s%s' % (settings.MEDIA_URL, file_path)}

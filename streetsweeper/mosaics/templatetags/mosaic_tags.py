from django import template


register = template.Library()


@register.inclusion_tag('mosaics/includes/mosaic.html')
def show_mosaic(mosaic, width, height, edge_height, xoffset):
    # Define the filename for the mosaic image that's going to be created
    # If this file already exists, just return it
    # TODO: gather tiles required to render area of mosaic defined by parameters
    # Create PIL image
    # Open each tile and place it in the PIL image at the appropriate coordinates
    # Save the image to the generated filename
    # return the filename (to the template, which should generate the image tag)
    return {}

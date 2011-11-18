from mezzanine.pages.page_processors import processor_for
from views import index_handle, get_button, remove_button

__author__ = 'fatrix'

@processor_for('apps/buttonizer')
def page(request, page):
    if "get" in request.GET:
        return get_button(request, guid=request.GET.__getitem__('get'))
    if "remove" in request.GET:
        return remove_button(request, guid=request.GET.__getitem__('remove'))
    return index_handle(request)

from mezzanine.pages.page_processors import processor_for
from views import index_handle, get_button, remove_button, new_button
from django.conf import settings

@processor_for(settings.PICASABUTTONIZER_SLUG)
def page(request, page):
    action = request.GET.get('action', None)
    guid = request.GET.get('guid', None)
    type = request.GET.get('type', None)
    print action
    print "hallooo"
    #if not action:
    #    return None
    #else:
    if action == "get":
        return get_button(request, guid)
    if action == "remove":
        return remove_button(request, guid)
    if type:
        return new_button(request, type=type)
    return index_handle(request, guid)

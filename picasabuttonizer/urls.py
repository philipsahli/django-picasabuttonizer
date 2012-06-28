__author__ = 'fatrix'
from django.conf.urls.defaults import *

from xcore import urls
urlpatterns = patterns('',
    #url(r'^$', 'picasabuttonizer.views.index', name="buttonizer"),
    #url(r'^button/edit/(?P<guid>[0-9a-zA-Z-_]+)/$', 'picasabuttonizer.views.index', name="buttonizer_edit_button"),
    #url(r'^button/get/(?P<guid>[0-9a-zA-Z-_]+)/$', 'picasabuttonizer.views.get_button', name="buttonizer_get_button"),
    #url(r'^button/remove/(?P<guid>[0-9a-zA-Z-_]+)/$', 'picasabuttonizer.views.remove_button', name="buttonizer_remove_button"),
)
try:
    import mezzanine
except ImportError, e:
   urlpatterns += patterns('',
       url(r'^$', 'picasabuttonizer.views.index', name="buttonizer"),
   )


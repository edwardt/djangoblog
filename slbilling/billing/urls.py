from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', list),
    (r'^archive/(?P\d{1,2}/$', list),
    (r'^\d{4}/d{1,2}/(?P.*)/$', detail),
    (r'^(?P\d{4})/(?P\d{1,2})/$', month),
    (r'^(?P\d{4})/$', year),
    (r'^category/$', category),     
    (r'^category/(?P.*)/$', one_category),     
    (r'^tag/$', tag),     
    (r'^tag/(?P.*)/$', one_tag), )
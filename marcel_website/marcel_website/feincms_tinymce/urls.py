""" Add this url path to your patterns:

    url(r'', include('feincms_tinymce.urls')),

"""

from django.conf.urls import *

urlpatterns = patterns('feincms_tinymce.views',
    url(r'^ajax/pageurl/$', 'pageurl', name='feincms_linklist_pageurl'),
)

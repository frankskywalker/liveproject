from django.conf.urls import *
from liveupdate.models import Update

urlpatterns = patterns('',
                       url(r'^updates-after/(?P<id>\d+)/$',
                           'liveupdate.views.updates_after'),
                       )

urlpatterns += patterns('django.views.generic',
                        url(r'^$', 'list_detail.object_list', {
                            'queryset': Update.objects.all()
                        }),
                        )
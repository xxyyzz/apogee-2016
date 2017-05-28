from Event import views
from django.conf.urls import url
urlpatterns = [
    url(r'^get_event/(?P<event_id>[0-9]+)/$', views.geteventdata, name='get'),
    # url(r'^notify/(?P<notification_id>[0-9]+)/$', views.getnotificationdata, name='notifications'),
    # url(r'^category/(?P<category>.*)/$', views.categorywise, name='get'),
    url(r'^summary/$', views.summary, name='summary'),
]

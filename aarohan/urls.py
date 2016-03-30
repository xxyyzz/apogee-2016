from aarohan import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', views.website),
    url(r'^software/cl09', views.soft09),
    url(r'^software/cl10', views.soft10),
    url(r'^software/cl11', views.soft11),
    url(r'^software/cl12', views.soft12),
    url(r'^aarohan_results', views.results),

    ]

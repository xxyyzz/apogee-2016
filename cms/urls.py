from django.conf.urls import include, url
from cms import views

urlpatterns = [
    url(r'^paperstats/', views.paper_stats_xlsx),
]
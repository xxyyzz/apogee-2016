from django.conf.urls import include, url
from cms import views

urlpatterns = [
    url(r'^paperxlsx/', views.paper_stats_xlsx),
    url(r'^projectxlsx/', views.project_stats_xlsx),
]
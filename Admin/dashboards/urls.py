from django.urls import path
from dashboards.views import (
    dashboard_view,
    dashboard_analytics_view,
    dashboard_crm_view,
    dashboard_learning_view,
    dashboard_estate_view,
)

app_name = 'dashboards' 

urlpatterns = [
    path('',dashboard_view,name="dashboard"),
    path('dashboard-analytics',dashboard_analytics_view,name="dashboard-analytics"),
    path('dashboard-crm',dashboard_crm_view,name="dashboard-crm"),
    path('dashboard-learning',dashboard_learning_view,name="dashboard-learning"),
    path('dashboard-real-estate',dashboard_estate_view,name="dashboard-real-estate"),
]
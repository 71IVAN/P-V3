from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Dashboardview(LoginRequiredMixin,TemplateView):
    pass

dashboard_view = Dashboardview.as_view(template_name = "dashboards/index.html")
dashboard_analytics_view = Dashboardview.as_view(template_name = "dashboards/dashboard-analytics.html")
dashboard_crm_view = Dashboardview.as_view(template_name = "dashboards/dashboard-crm.html")
dashboard_learning_view = Dashboardview.as_view(template_name = "dashboards/dashboard-learning.html")
dashboard_estate_view = Dashboardview.as_view(template_name = "dashboards/dashboard-real-estate.html")

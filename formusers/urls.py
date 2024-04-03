from django.urls import path
from .views import DashboardView, FormUsersView, FormUserPost

urlpatterns = [
path ('formusers',FormUsersView.as_view(),name='seeFormusers'),
path('saveformusers',FormUserPost.as_view(),name='saveFormusers'),
path('dashboard',DashboardView.as_view(),name='dashboard'),
]
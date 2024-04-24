from django.urls import path
from . import views

urlpatterns = [
    path('vista', views.seeViewApp.as_view(), name='verAppBootstrap'),
]
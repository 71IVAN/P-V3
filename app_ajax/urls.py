from django.urls import path
from . import views

urlpatterns = [
    path('ajax', views.UsersList.as_view(), name='ajaxViewSee'),
]
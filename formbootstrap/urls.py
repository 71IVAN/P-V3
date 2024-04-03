from django.urls import path
from formbootstrap.views import  SeeBootstrapForm, saveBootstrapForm,goDashboard

urlpatterns = [
    path('verform', SeeBootstrapForm.as_view(), name='seeFormBootstrap'),
    path('guardarform', saveBootstrapForm.as_view(), name='saveFormBootstrap'),
    path('salida', goDashboard.as_view(), name='goDashboard'),
    ]

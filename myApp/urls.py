from django.urls import path
from myApp.views import SaveForm, seemyApp, goDashboard

urlpatterns = [
    path('seemyform',seemyApp.as_view(), name="seeMyForm"),
    path('guardarform', SaveForm.as_view(),name="SaveFormMyApp"),
    path('dashboard', goDashboard.as_view(),name="goDashboard"),
]
 
from django.urls import path
from terceros import views
# from components import views

urlpatterns = [
    path('mostrar',views.SeeForm.as_view(),name="seeForm"),
    path('guardarform',views.SaveForm.as_view(),name="SaveForm")
]

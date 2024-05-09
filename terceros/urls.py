from django.urls import path
from terceros.views import FormThirdViews

urlpatterns = [
    path('formthird/', FormThirdViews.as_view(), name="ViewsThird"),
]

from django.urls import path
from layouts.views import (
    horizontal_layouts,
    detached_layouts,
    two_column_layouts,
    vertical_hovered_layouts,
)

app_name = 'layouts'

urlpatterns = [
    
    path('horizontal',horizontal_layouts,name="horizontal"),
    path('detached',detached_layouts,name="detached"),
    path('two_column',two_column_layouts,name="two_column"),
    path('vertical-hovered',vertical_hovered_layouts,name="vertical-hovered"),
 
]
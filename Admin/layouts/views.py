from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class layoutsview(TemplateView):
    pass

horizontal_layouts = layoutsview.as_view(template_name = "layouts/layouts-horizontal.html")
detached_layouts = layoutsview.as_view(template_name = "layouts/layouts-detached.html")
two_column_layouts = layoutsview.as_view(template_name = "layouts/layouts-two-column.html")
vertical_hovered_layouts = layoutsview.as_view(template_name = "layouts/layouts-vertical-hovered.html")

from django.shortcuts import render
from django.views import View

# Create your views here.
class seeViewApp(View):
    def get(self, request):
        return render(request, 'components/forms/components-formappBootstrap.html')
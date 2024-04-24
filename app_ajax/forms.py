from django import forms
from django.http import JsonResponse
import requests

class UserForm(forms.Form):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['submit'] = forms.SubmitField(label='Submit')
        
    def handle_ajax(self, request):
        """
        Realizar una peticion AJAX a la vsita 'users_list'
        """
        
        response = requests.get(f'{request.META["HTTP_HOST"]}{request.META["PATH_INFO"]}',
                                headers={'X-CSRFToken': request.COOKIES['csrftoken']},
                                )
        return JsonResponse(response.json())
        
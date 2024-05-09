from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from skote.validations import utilities
from terceros.models import ModelThird
from .forms import ThirdForm

class FormThirdViews(View):
    def get(self, request):
        form = ThirdForm()  # Instancia del formulario
        data = {
            'form':form
        }
        return render(request, 'components/forms/components-terceros.html', data)
    
    def post(self,request):
        if utilities.is_ajax(request):
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            identity_document = request.POST.get('identity_document')
            hora = request.POST.get('hora')
            
            message = "Usuario Nuevo " + name + " email: "
            state = True
            new_object = ModelThird.objects.create(
                name=name,
                email=email,
                phone=phone,
                identity_document=identity_document,
                hora=hora,
            )
            
            data = {
                'state': state, 
                'message': message + email
            }
            
        else:
            data = {'state': False, 'message': 'No es ajax'}
        
        return JsonResponse(data)
            
                
                
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
                
                
                
# form = ThirdForm(request.POST)
#                 if form.is_valid():
#                     name = request.POST.get('name')
#                     email = request.POST.get('email')
#                     phone = request.POST.get('phone')
#                     identity_document = request.POST.get('identity_document')
#                     hora = request.POST.get('hora')
                    
#                     new_object = ModelThird.objects.create(
#                         name=name,
#                         email=email,
#                         phone=phone,
#                         identity_document=identity_document,
#                         hora=hora,
#                     )
                    
#                     return JsonResponse({'state': True})
#                 else:
#                     return JsonResponse(form.errors)
#             else:
#                 return JsonResponse({'error': 'Invalid content type...'})


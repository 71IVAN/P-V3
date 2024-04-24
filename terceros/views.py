from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .models import ModelThird
from .forms import ThirdForm

class SeeForm(View):
    def get(self, request):
        form = ThirdForm()  # Instancia del formulario
        show_alert = request.GET.get('alert')
        data = {
            'form':form
        }
        return render(request, 'components/forms/components-terceros.html', data)

class SaveForm(View):
    def post(self, request):
        newObject = None
        if request.method == 'POST':
            form = ThirdForm(request.POST)
            if form.is_valid():
                
                #Obetener datos 
                name = request.POST.get('name')
                email = request.POST.get('email')
                phone = request.POST.get('phone')
                address = request.POST.get('address')
                typeThird = request.POST.get('typeThird')
                activo = request.POST.get('activo')
                description = request.POST.get('description')
                identity_document = request.POST.get('identity_document')
                hora = request.POST.get('hora')
                
                #Nueva instancia del modelo y guardar los datos en la base de datos
                newObject = ModelThird.objects.create(
                    name=name,
                    email=email,
                    phone=phone,
                    address=address,
                    typeThird=typeThird,
                    activo=activo,
                    description=description,
                    identity_document=identity_document,
                    hora=hora,
                )

                # Redirigir a una pagina
                messages.success(request, 'Your form has been submitted successfully!')
                return redirect('seeForm')
        else:
            form = ThirdForm()
        return render(request, 'components/forms/components-terceros.html', {'form': form})
 
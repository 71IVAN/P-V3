from audioop import reverse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from myApp.forms import myForm
from myApp.models import modeltest
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password


class seemyApp(FormView):
    template_name = 'components/forms/components-myapp.html'
    form_class = myForm

class SaveForm(FormView):
    template_name = 'components/forms/components-myapp.html'
    form_class = myForm
    success_url = reverse_lazy('seeMyForm')

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']        
        email = form.cleaned_data['email']
        telefono = form.cleaned_data['telefono']
        address = form.cleaned_data['address']
        typeThird = form.cleaned_data['typeThird']
        activo = form.cleaned_data['activo']
        identity_document = form.cleaned_data['identity_document']
        
        password = get_random_string(length=12)
        
        hashed_password = make_password(password)
        new_object = modeltest(
            nombre = nombre, 
            email = email,
            telefono = telefono, 
            address = address,
            typeThird = typeThird,
            activo = activo,
            identity_document = identity_document,
            password = hashed_password
        )
        new_object.save()
        
        if new_object:
            messages.success(self.request, 'Your form has been submitted successfully!')
        
        else:
            messages.error(self.request, 'Your form has not been submitted successfully!')
        
        return super(SaveForm, self).form_valid(form)

class goDashboard(FormView):
    template_name = 'dashboard/dashboard.html'
    form_class = myForm

# class UpdateUserView(FormView):
#     template_name = 'components/forms/components-formsuser.html'
#     form_class = myForm

#     def traerForm(self, request, form):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})
    
#     def actualizarForm(self, request, form):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(request, {'form':form})
        
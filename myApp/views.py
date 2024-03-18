from audioop import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from myApp.forms import myForm
from django.core.exceptions import ValidationError
from myApp.models import modeltest

class seemyApp(FormView):
    template_name = 'components/forms/components-myapp.html'
    form_class = myForm

class SaveForm(FormView):
    template_name = 'components/forms/components-myapp.html'
    form_class = myForm
    success_url = reverse_lazy('seeMyForm')

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        # if len(nombre) <= 3:
        #     raise ValidationError('El nombre debe tener mas de 3 caracteres')        
         
        email = form.cleaned_data['email']
        telefono = form.cleaned_data['telefono']
        address = form.cleaned_data['address']
        typeThird = form.cleaned_data['typeThird']
        activo = form.cleaned_data['activo']
        identity_document = form.cleaned_data['identity_document']
        
        new_object = modeltest(
            nombre = nombre,
            email = email,
            telefono = telefono,
            address = address,
            typeThird = typeThird,
            activo = activo,
            identity_document = identity_document
        )

        new_object.save()
        messages.success(self.request, 'Your form has been submitted successfully!', extra_tags='form-id')
        return super(SaveForm, self).form_valid(form)

class goDashboard(FormView):
    template_name = 'dashboard/dashboard.html'
    form_class = myForm

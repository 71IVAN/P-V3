from django.contrib import messages
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from formbootstrap.forms import FormBootstrap
from formbootstrap.models import modelBoostrap

class SeeBootstrapForm(FormView):
    template_name = 'components/forms/components-formbootstrap.html'
    form_class = FormBootstrap
    
class saveBootstrapForm(FormView):
    template_name = 'components/forms/components-formbootstrap.html'
    form_class = FormBootstrap
    success_url = reverse_lazy('goDashboard')
    
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        ide = form.cleaned_data['ide']
        phone = form.cleaned_data['phone']
        description = form.cleaned_data['description']
        address = form.cleaned_data['address']
        activo = form.cleaned_data['activo']
        typethird = form.cleaned_data['typethird']
        
        newObject = modelBoostrap(
            name = name,
            email = email,
            ide = ide,
            phone = phone,
            description = description,
            address = address,
            activo = activo,
            typethird = typethird
        )
        
        newObject.save()
        if newObject:
            messages.success(self.request, 'Your form has been submitted successfully!', extra_tags='form-id')
        
        else:
            messages.error(self.request, 'Your form has not been submitted successfully!', extra_tags='form-id')

        return super(saveBootstrapForm, self).form_valid(form)
    
class goDashboard(FormView):
    template_name = 'dashboard/dashboard.html'
    form_class = FormBootstrap
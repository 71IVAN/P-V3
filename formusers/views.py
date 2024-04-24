from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import formUser
from django.views.generic import FormView
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.contrib import messages


class DashboardView(LoginRequiredMixin, FormView):
    template_name = 'dashboard/dashboard.html'
    def get(self, request):
        return render(request, self.template_name)

class FormUsersView(LoginRequiredMixin, FormView):
    template_name = 'components/forms/components-formsuser.html'
    form_class = formUser
    
class FormUserPost(LoginRequiredMixin, FormView):
    template_name = 'components/forms/components-formsuser.html'
    form_class = formUser
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        username = form.cleaned_data['username']
        date_joined_default = timezone.now() 
        
        password = get_random_string(length=12)
        hashed_password = make_password(password)

        new_object = form.save(commit=False)
        new_object.first_name = first_name
        new_object.last_name = last_name
        new_object.email = email
        new_object.username = username
        new_object.password = hashed_password
        new_object.date_joined = date_joined_default
        new_object.save()
        
        messages.success(self.request, 'Your form has been submitted successfully!')
        print("Formulario guardado con exito")

        return super().form_valid(form)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# class UpdateUserView(LoginRequiredMixin, FormView):
#         template_name = 'components/forms/components-formsuser.html'

#         def edicionForm(self, request, form):
#             form = form
#             return render(request, {'form':form})
        
    
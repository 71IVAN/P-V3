from django.contrib.auth.models import User
from django import forms

class formUser(forms.ModelForm):
    first_name = forms.CharField(
        help_text="ejm: Alexander Anderson",
        # required=True,
        widget=forms.TextInput(attrs={"placeholder": "Primer nombre por favor", 'id':'first_name' }),
        label="Primer Nombre",
    )
    
    last_name = forms.CharField(
        help_text="ejm: Perez",
        # required=True,
        widget=forms.TextInput(attrs={"placeholder": "Apellidos", 'id':'last_name'}),
    )
    
    email = forms.EmailField(
        help_text="ejm: javier4@example.com",
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Email", 'id':'email'}),
    )
    
    # username = forms.CharField(
    #     # help_text="ejm: javier87",
    #     required=True,
    #     widget=forms.TextInput(attrs={"placeholder": "Username", 'id':'username'}),
    # )
    
    is_active = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"id":"is_active"}),
    )
    
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['password', 'date_joined','is_staff','is_superuser','last_login']
        
        
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name) <= 3:
            raise forms.ValidationError("El nombre debe tener más de 3 caracteres")
        elif first_name == '':
            raise forms.ValidationError("El nombre no puede estar vacío")
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if len(last_name) <= 2:
            raise forms.ValidationError("Los apellidos deben tener más de 2 caracteres")
        return last_name
    
    def clean_email(self):
        email = self.cleaned_data['email']
        allowed_domains = ['com', '.net', '.in', '.org']
        if not any(email.endswith(domain) for domain in allowed_domains):
            raise forms.ValidationError("El correo electrónico no es válido. Por favor, ingrese un dominio válido.")
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 3:
            raise forms.ValidationError("El nombre de usuario debe tener más de 3 caracteres")
        return username 
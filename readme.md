Crispy_Forms:
Es una biblioteca de Python que se integra con Django para proporcionar una forma más elegante y flexible de renderizar formularios HTML.

-Instalando django-crispy-forms:
pip install django-crispy-forms

-Agregue ‘crispy_forms’ a INSTALLED_APPS en settings.py:
"crispy_forms",

-Agregar bootstrap5 en settings.py si desea implemntar este framework con crispy_forms:
CRISPY_TEMPLATE_PACK = "bootstrap5"

Como inplementar crispy_forms:
Cargar y utilizar las siguientes etiquetas 
{% load crispy_forms_tags %}
{{ form|cripsy }} or  {{form.fields|as_crispy_field}}

crys_forms con bootstrap5
-Crear modelo en (models.py)
-Crear formulario en (forms.py) 
-Crear vistas (save o see) en views.py 

Templates:
Usar extends para traer una base de html donde se encuentren importados los archivos que se utilizaran para el desarrollo de los templates
(.js, css, bootstrap etc)

Nota:Para usar ambas herramientas (crispy_forms y bootstrap) usaremos divs y clases para contruir la arquitectura del formualario a neustros gustos, ejemplo:                 <div class="row" >
                                           <div class="form-group col-md-6 mb-0">
                                            {{form.name|as_crispy_field}}
                                           </div>

                                             
{{form.name_fields|as_crispy_field}} nos ayudara a traer los campos a nuestro gusto, podremos poner el orden que nos guste. 

-------------------------------------------------------------------------------------------------------------------------------------------   

Crispy Forms es una biblioteca de Python para Django que se centra en la presentación y organización de formularios HTML de manera elegante y eficiente. 
Su función principal es mejorar la experiencia de desarrollo al permitir definir la apariencia y el diseño de los formularios de manera más concisa y estructurada.

Ventajas:

1. Sintaxis Concisa: Crispy Forms permite definir la apariencia y el diseño de los formularios directamente en el código Python utilizando una sintaxis clara y concisa.

2. Integración con Bootstrap: Crispy Forms se integra bien con el framework de diseño Bootstrap, lo que facilita la creación de formularios con un aspecto moderno y responsivo.

3. Reutilización de Diseño: Permite definir layouts de formularios reutilizables, lo que simplifica el mantenimiento y la consistencia del diseño en toda la aplicación.

4. Facilidad de Personalización: Crispy Forms ofrece una amplia gama de opciones de personalización para adaptar el diseño de los formularios según las necesidades específicas del proyecto.

5. Soporte para Diferentes Estilos de Diseño: Además de Bootstrap, Crispy Forms es compatible con otros frameworks de diseño como Foundation, lo que brinda flexibilidad en la elección del estilo de diseño de los formularios.

Validacion de formulario Python django:
Proceso de verificar y asegurar que los datos ingresados por los usuarios en formularios de Django cumplan con los criterios definidos, como el formato correcto, la longitud adecuada y la ausencia de errores.

Validacion de datos

Example:
from django import forms

forms.py  
class PersonForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100)
    date_of_birth = forms.DateField(label='Date of Birth')
    address = forms.CharField(label='Address', max_length=200)
    phone_number = forms.CharField(label='Phone Number', max_length=15)
    email = forms.EmailField(label='Email')
    identity_document = forms.CharField(label='Identity Document', max_length=20)

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PersonForm


views.py 
def save_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            # Procesar y guardar los datos del formulario en la base de datos
            full_name = form.cleaned_data['full_name']
            date_of_birth = form.cleaned_data['date_of_birth']
            address = form.cleaned_data['address']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            identity_document = form.cleaned_data['identity_document']
            
            # Aquí puedes guardar los datos en la base de datos o hacer cualquier otra acción necesaria
            
            # Redirigir a una página de éxito o mostrar un mensaje de éxito
            return HttpResponseRedirect('/success/')  # Cambia '/success/' por la URL de tu página de éxito
    else:
        form = PersonForm()
    
    # Renderizar el formulario en la página
    return render(request, 'person_form.html', {'form': form})




Ejemplos de Validacion:

cleaned_data:

Definición: cleaned_data es un diccionario que contiene los datos limpios y validados de un formulario después de que se ha llamado al método is_valid().
Ejemplo: full_name = form.cleaned_data['full_name']

max_length:

Definición: max_length es un validador que limita la longitud máxima de un campo de texto.
Ejemplo: forms.CharField(max_length=100)

required:

Definición: required es un validador que indica que un campo es obligatorio y no puede estar vacío.
Ejemplo: forms.CharField(required=True)

password:

Definición: password es un validador que se utiliza comúnmente para validar contraseñas. Puede incluir reglas como longitud mínima, caracteres especiales requeridos, etc.
Ejemplo:
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)


EmailValidator:

Definición: EmailValidator es una clase de validador integrada en Django que verifica si un valor dado es una dirección de correo electrónico válida.
Ejemplo:
from django.core.validators import EmailValidator

email = forms.CharField(validators=[EmailValidator])

RegexValidator:

Definición: RegexValidator permite validar un campo basado en una expresión regular específica.
Ejemplo:
from django.core.validators import RegexValidator

phone_number = forms.CharField(validators=[RegexValidator(regex=r'^\d{10}$', message='Enter a valid phone number')])

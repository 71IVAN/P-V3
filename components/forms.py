from django import forms 

class ContactForm(forms.Form):
    firstname = forms.CharField(label='Your Name', max_length=100)
    lastname = forms.CharField(label='Your last name', max_length=100)
    phone = forms.CharField(label='Your number')
    email = forms.EmailField(label='Your email', max_length=100)
    address = forms.CharField(label='Your address', max_length=70)
    genderAll = forms.CharField(label='Your type', max_length=20)
     
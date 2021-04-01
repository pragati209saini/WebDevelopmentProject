from django import forms
from contact.models import contactu
from django.forms import ModelForm

class contactForm(forms.ModelForm):
    class Meta:
        model = contactu
        fields = '__all__'
from django import forms
from registration.models import donor
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class donorRegistration(ModelForm):
    class Meta:
        model = donor
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'gender' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'date_of_birth' : forms.DateInput(attrs={'class':'form-control', 'type':'date', 'required':'True'}),
            'blood_group' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'phone_number' : forms.NumberInput(attrs={'class':'form-control', 'required':'True'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'required':'True'}),
            'occupation' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'last_donate_date' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'any_diseases' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'allergies' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'cardiac' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'bleeding_disorders' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'hbsAg_hcv_hIV' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control', 'required':'True'}),

        }




class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

from django.shortcuts import render, redirect
from registration.models import donor
from registration.forms import donorRegistration
from django.contrib import messages, auth

def register(request):
    forms = donorRegistration()
    if request.method == 'POST':
        forms = donorRegistration(request.POST)
        if forms.is_valid():
            forms.save()
            
            return render(request, 'donar_reg_s.html',{'forms' : forms})
    return render(request, 'register.html',{'forms' : forms})
     


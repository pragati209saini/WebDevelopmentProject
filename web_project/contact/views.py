from django.shortcuts import render
from contact.models import contactu
from contact.forms import contactForm

# Create your views here.

def contact(request):
    if request.method =='POST':
     firstname = request.POST['firstname']
     lastname = request.POST['lastname']
     country = request.POST['country']
     subject = request.POST['subject']
     pic = contactu(firstname=firstname,lastname=lastname,country=country,subject=subject)
     pic.save()

    return render(request,'contact.html')
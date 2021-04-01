from django.shortcuts import render
from .forms import DonorSearch
from registration.models import donor
from .models import SearchLogo


def searchdisplay(request):
    search_forms = DonorSearch()
    if request.method == 'POST':
        search_forms = DonorSearch(request.POST)
        if search_forms.is_valid():
            blood_group = search_forms.cleaned_data['select_blood_group']
            donor_filter = donor.objects.filter(blood_group=blood_group)
            context = {
                'donor_filter' : donor_filter
            }
            return render(request, 'donor_list.html', context)



    context = {
        'forms_search' : search_forms,
    }
    return render(request, 'donor_search.html' ,context)




def donorlistdetail(request, email):
    email = email
    detail = donor()
    detail = donor.objects.get(email=email)
    context = {
        'details' : detail
    }
    return render(request, 'donor_l_d.html', context)


from django.shortcuts import render, redirect



def home(request):  
 return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def group(request):
    return render(request,"group.html")


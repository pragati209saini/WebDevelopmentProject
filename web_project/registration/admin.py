from django.contrib import admin
from .models import donor

# Register your models here.
class DonorListShow(admin.ModelAdmin):
    list_display = ['name', 'blood_group']

admin.site.register(donor,DonorListShow)
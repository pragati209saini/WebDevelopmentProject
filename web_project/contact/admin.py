from django.contrib import admin
from contact.models import contactu
# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','country','subject']

admin.site.register(contactu,contactAdmin) 


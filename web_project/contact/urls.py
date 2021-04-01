from django.urls import path
from .views import contact

urlpatterns = [
    path(r'^contact',contact,name='contact'),
 ]

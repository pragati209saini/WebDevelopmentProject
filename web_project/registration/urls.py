from django.urls import path
from .views import register

urlpatterns = [
    path(r'^register',register,name='register'),
    path(r'donors',register , name='dregdisplay'),

]

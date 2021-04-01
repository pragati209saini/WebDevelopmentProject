from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.home,name='home'),
    path(r'^about',views.about,name='about'),
      path(r'^info',views.group,name='group'),

]
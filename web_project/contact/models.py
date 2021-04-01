from django.db import models

# Create your models here.
class contactu(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=25)
    country = models.CharField(max_length=25)
    subject = models.CharField(max_length=500)

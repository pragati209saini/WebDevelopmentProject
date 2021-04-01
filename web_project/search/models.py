from django.db import models

# Create your models here.
class SearchLogo(models.Model):
    title = models.CharField(blank=True, null=True, max_length=10)
    logo_number = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.title

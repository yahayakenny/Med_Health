from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Specialty(models.Model):
    specialty_name = models.CharField(max_length=200, blank=True , null=True)
    specialty_description = models.CharField(max_length=200, blank=True , null=True)

    def __str__(self):
        return self.specialty_name
     

class Doctor(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(null = True, blank = True)
    specialty = models.ForeignKey(Specialty, null = True, blank = True, on_delete = models.SET_NULL)
    university = models.CharField(max_length=100, blank=True , null=True)
    qualifications = models.CharField(max_length=100, blank=True , null=True)
    information= models.CharField(max_length= 500, blank=True , null=True)

    def __str__(self):
        return self.name



from django.db import models
from doctor_app.models import Specialty
from django.contrib.auth.models import User

# Create your models here.

class BookDoctor(models.Model):
    CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    patient_name = models.CharField(null = True, blank = True, max_length=100)
    patient_age = models.IntegerField(default = 0)
    patient_gender = models.CharField(max_length=100, choices= CHOICES, blank=True , null=True)
    patient_specialty = models.ForeignKey(Specialty, null = True, blank = True, on_delete = models.SET_NULL)
    patient_complaint = models.CharField(max_length=200, blank=True , null=True)
    date_booked = models.DateTimeField(auto_now_add=True)
    appointment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_complaint

   
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank = True, null = True, default = 'default.jpg')
    def __str__(self):
        return self.user.username
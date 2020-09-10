from django import forms
from patient_app.models import BookDoctor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BookDoctorForm(forms.ModelForm):
    class Meta:
        model = BookDoctor
        fields = ( 'patient_complaint', 'patient_specialty', 'patient_age', 'patient_gender')


class UserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2' )

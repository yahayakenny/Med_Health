from django.shortcuts import render
from doctor_app.models import Doctor
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'index.html', {'doctors': doctors})

def welcome(request):
    return render(request, 'doctors/welcome.html')
    
@login_required
def doctor_detail(request, doctor_id):
    details = Doctor.objects.get(id = doctor_id)
    return render(request, 'doctors/doctor_detail.html', {'details': details})


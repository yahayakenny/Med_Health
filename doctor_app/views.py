from django.shortcuts import render
from doctor_app.models import Doctor
from django.contrib.auth.decorators import login_required
from doctor_app.filters import DoctorFilter

def home(request):
    doctors = Doctor.objects.all()
    doctor_filters = DoctorFilter(request.GET, queryset = doctors)
    doctors = doctor_filters.qs
    context = {'doctors': doctors}
    return render(request, 'index.html', {'doctors': doctors, 'doctor_filters': doctor_filters})
 
@login_required
def doctor_detail(request, doctor_id):
    details = Doctor.objects.get(id = doctor_id)  
    return render(request, 'doctors/doctor_detail.html', {'details': details})


def map(request):
    return render(request, 'maps.html')
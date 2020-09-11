from django.shortcuts import render, redirect
from patient_app.models import BookDoctor, Profile
from patient_app.forms import BookDoctorForm
from patient_app.forms import UserForm
from django.contrib import messages
from doctor_app.models import Specialty
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.
@login_required
def dashboard(request):
    patients = BookDoctor.objects.all()
    profile = Profile.objects.all()
    return render(request, 'patients/dashboard.html', {'profile': profile, 'patients': patients})

@login_required
def book_appointment(request):
    form = BookDoctorForm()
    patients = BookDoctor.objects.all()
    specialty = Specialty.objects.all()
    if request.method == 'POST':
        form = BookDoctorForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    
    # send_mail(
    #     'New Patient appointment',
    #     'You have a new appointment with a patient, sign into admin panel for more info',
    #     'yahayakehinde911@gmail.com',
    #     ['y.hkehinde@yahoo.com'],
    #     fail_silently=False

    # )

    context = {'form': form, 'specialty': specialty, 'patients': patients}
    return render(request, 'patients/book_apt.html', context)

@login_required
def delete(request, patient_id):
    patient_delete = BookDoctor.objects.get(id = patient_id)
    patient_delete.delete()
    return redirect('dashboard')

@login_required
def update(request, patient_id):
    patient_update = BookDoctor.objects.get(id = patient_id)
    form = BookDoctorForm(instance= patient_update)
    if request.method == 'POST':
        form = BookDoctorForm(request.POST, instance=patient_update)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'patients/book_apt.html', context)


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Thank you for registering with us {username}')
            form.save()
            return redirect ('login')       
    else:
        form = UserForm()
        
    return render(request, 'patients/register.html', {'form': form})

@login_required
def patient_detail(request, mypatient_id):
    details = BookDoctor.objects.get(id = mypatient_id)
    return render(request, 'patients/patient_detail.html', {'details': details})
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Hospital, Doctor, Patient, Appointment
from .forms import HospitalForm, DoctorForm, PatientForm, AppointmentForm
from django.db.models import Count
from django.db.models.functions import TruncMonth
from datetime import datetime
import json
from django.utils import timezone
from collections import defaultdict



#           --------------------------------------------  Auth Views   -----------------------------------------------


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def home(request):
    
    doctor_count = Doctor.objects.count()
    appointment_count = Appointment.objects.count()

   
    doctor_appointments = defaultdict(int)  
    appointments = Appointment.objects.all()

   
    for appointment in appointments:
        doctor_appointments[appointment.doctor_id] += 1

    
    doctor_names = [] 
    appointment_data = []  

    for doctor in Doctor.objects.all():
        doctor_names.append(doctor.name)  
        appointment_data.append(doctor_appointments[doctor.id]) 

 
    context = {
        'username': request.user.username,
        'doctor_names': json.dumps(doctor_names),
        'appointment_data': json.dumps(appointment_data),
    }

    return render(request, 'home.html', context)



#           --------------------------------------------  Hospital CRUD   -----------------------------------------------
@login_required
def hospital_create(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('hospital_list')
    
    else:
        form = HospitalForm()
    
    return render(request, 'hospital_form.html', {'form':form})


@login_required
def hospital_list(request):
    hospitals = Hospital.objects.all()

    return render(request, 'hospital_list.html', {'hospitals':hospitals})


@login_required
def hospital_update(request, pk):
    hospital = get_object_or_404(Hospital, pk = pk)

    if request.method == 'POST':
        form = HospitalForm(request.POST, instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('hospital_list')
    
    else:
        form = HospitalForm(instance=hospital)
    
    return render(request,'hospital_form.html',{'form':form}) # personal logic


@login_required
def hospital_delete(request, pk):
    hospital = get_object_or_404(Hospital, pk = pk)

    if request.method == 'POST':
        hospital.delete()
        return redirect('hospital_list')

    return render(request,'hospital_confirm_delete.html',{'hospital':hospital} )



#           💊--------------------------------------------  Patient CRUD   -----------------------------------------------💉

@login_required
def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')

    else:
        form = PatientForm()
    return render(request, 'patient_form.html', {'form': form})


@login_required
def patient_list(request):
    patients = Patient.objects.all()

    return render(request, 'patient_list.html', {'patients':patients})


@login_required
def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patient_form.html', {'form': form})


@login_required
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'patient_confirm_delete.html', {'patient': patient})


#           --------------------------------------------  Doctor CRUD   -----------------------------------------------

@login_required
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})


@login_required
def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'doctor_form.html', {'form': form})


@login_required
def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctor_form.html', {'form': form})


@login_required
def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'doctor_confirm_delete.html', {'doctor': doctor})


@login_required
def create_appointment(request):
    if request.method == 'POST':        
        form = AppointmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('appointment_list')
        
    else:
        form = AppointmentForm()
    
    return render(request,'appointment_form.html',{'form':form})


@login_required
def appointment_list(request):
    appointments = Appointment.objects.all()

    return render(request,'appointment_list.html',{'appointments':appointments})


@login_required
def update_appointment(request,pk):
    appointment = get_object_or_404(Appointment,pk = pk)

    if request.method == 'POST':
        form = AppointmentForm(request.POST,instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    
    else:
        form = AppointmentForm(instance=appointment)
    
    return render(request,'appointment_form.html',{'form':form})


@login_required
def delete_appointment(request,pk):
    appointment = get_object_or_404(Appointment, pk = pk)

    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    
    return render(request, 'appointment_confirm_delete.html', {'appointment': appointment})



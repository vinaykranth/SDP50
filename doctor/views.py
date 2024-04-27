from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'doctor/home.html')

from .models import Appointment

def view_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'view_appointment.html', {'appointments': appointments})

def give_appointment(request):
    return render(request, 'doctor/give_appointment.html')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Appointment

@login_required
def doctor_dashboard(request):
    doctor = request.user.doctor
    appointments = Appointment.objects.filter(doctor=doctor).select_related('doctor')
    return render(request, 'doctor_dashboard.html', {'appointment': appointment})


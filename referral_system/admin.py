from django.contrib import admin
from .models import Hospital, Patient, Doctor, Appointment

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
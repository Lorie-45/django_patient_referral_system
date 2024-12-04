from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)
    # hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, related_name="doctors")

    def __str__(self):
        return f"{self.name}"


class Hospital(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"    


class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    contact = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, null=True)


    def __str__(self):
        return f" {self.name}"



class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    reason = models.TextField(null=True)
    # date = models.DateTimeField()

    def __str__(self):
       
        return f"Appointment: {self.patient} with {self.doctor}"
    
    
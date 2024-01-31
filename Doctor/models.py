from django.db import models


class Doctor(models.Model):
    Username = models.CharField(max_length=50, blank=True)
    Email = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)


class Appointment(models.Model):
    patient_name = models.CharField(max_length=255)
    appointment_date = models.DateField()

    def __str__(self):
        return f"{self.patient_name} - {self.appointment_date}"
from django.db import models
from django.urls import reverse


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ClinicType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ClinicServices(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Clinic(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(ClinicType, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, null=True)
    services = models.ManyToManyField(ClinicServices, null=True)
    telephone = models.CharField(max_length=12, null=True)
    address = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return '{0} ({1}) Адрес:{2}'.format(self.name, self.city, self.address)

    def get_absolute_url(self):
        return reverse('clinic-detail', args=[str(self.id)])


class DoctorSpecialization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    clinic = models.ManyToManyField(Clinic, null=True)
    experience = models.TextField(max_length=300, null=True)
    education = models.TextField(max_length=100, null=True)
    specialization = models.ManyToManyField(DoctorSpecialization, null=True)
    telephone = models.CharField(max_length=12, null=True)
    about = models.TextField(max_length=500, null=True)

    def __str__(self):
        return '{0} {1}'.format(self.last_name, self.first_name)


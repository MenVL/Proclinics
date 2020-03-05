from django.contrib import admin
from .models import City, Clinic, ClinicServices, ClinicType, Doctor, DoctorSpecialization

admin.site.register(City)
admin.site.register(Clinic)
admin.site.register(ClinicServices)
admin.site.register(ClinicType)
admin.site.register(Doctor)
admin.site.register(DoctorSpecialization)

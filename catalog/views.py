from django.shortcuts import render, get_object_or_404
from .models import Clinic, ClinicType, ClinicServices, City, Doctor, DoctorSpecialization
from django.views import generic


def index(request):
    clinics_count = Clinic.objects.all().count()
    doctors_count = Doctor.objects.all().count()
    return render(
        request,
        'index.html',
        context={'clinics_count': clinics_count, 'doctors_count': doctors_count}
    )


def clinics_list(request):
    clinic_list = Clinic.objects.all()[:10]
    return render(
        request,
        'clinic_list.html',
        context={'clinic_list': clinic_list}
    )


def clinics_list_city(request):
    city_list = City.objects.all()
    city_dict = {}
    sort_city_dict = {}
    for city in city_list:
        count = Clinic.objects.filter(city=city).count()
        if count > 0:
            city_dict.update({city.name: count})
    for city in sorted(city_dict.items(), key=lambda i:i[1], reverse=True):
        sort_city_dict.update({city[0]: city[1]})

    return render(
        request,
        'clinics_list_city.html',
        context={'city_dict': sort_city_dict}
    )


def clinics_city_detail(request, city):
    clinics = Clinic.objects.filter(city.name == city)
    return render(
        request,
        'clinics_list_city_name.html',
        context={'clinics': clinics,
                 'city': city}
    )



def doctors_list(request):
    doctor_list = Doctor.objects.all()[:10]
    return render(
        request,
        'doctor_list.html',
        context={'doctor_list': doctor_list}
    )


def clinic_detail(request, pk):
    clinic = get_object_or_404(Clinic, pk=pk)
    doctor_list = Doctor.objects.filter(clinic=clinic)
    return render(
        request,
        'clinic_detail.html',
        context={'clinic': clinic,
                 'doctor_list': doctor_list}
    )


def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(
        request,
        'doctor_detail.html',
        context={'doctor': doctor}
    )


from django.shortcuts import render, get_object_or_404
from .models import Clinic, ClinicType, ClinicServices, City, Doctor, DoctorSpecialization
from django.db.models import Count
from django.views import generic


def index(request):
    # Главная страница
    clinics_count = Clinic.objects.all().count()
    doctors_count = Doctor.objects.all().count()
    return render(
        request,
        'index.html',
        context={'clinics_count': clinics_count, 'doctors_count': doctors_count}
    )


def clinics_list(request):
    # Список мед всех клиник
    clinic_list = Clinic.objects.all()
    return render(
        request,
        'clinic_list.html',
        context={'clinic_list': clinic_list}
    )


def clinics_list_city(request):
    # Список городов и кол-во клиник в каждом из них
    city_list = City.objects.annotate(Count('clinic')).filter(clinic__count__gt=0).order_by('-clinic__count')
    return render(
        request,
        'clinics_list_city.html',
        context={'city_list': city_list}
    )


def clinic_list_services(request):
    # Поиск клиник по услуге с выводом количества клиник с этой слугой
    services = ClinicServices.objects.annotate(Count('clinic')).filter(clinic__count__gt=0).order_by('-clinic__count')
    return render(
        request,
        'clinic_list_services.html',
        context={'services': services}
    )


def clinic_services_detail(request, service):
    # Список клиник с определенной услуги
    clinics = Clinic.objects.filter(services__pk=service).distinct()
    service_name = ClinicServices.objects.get(pk=service)
    return render(
        request,
        'clinic_services_detail.html',
        context={'clinics': clinics,
                 'service_name': service_name}
    )


def clinic_city_detail(request, city):
    # Список клиник в городу
    clinics = Clinic.objects.filter(city__pk=city).distinct()
    city_name = City.objects.get(pk=city)
    return render(
        request,
        'clinic_city_detail.html',
        context={'clinics': clinics,
                 'city_name': city_name}
    )


def clinic_detail(request, pk):
    # Детальная информация о клинике
    clinic = get_object_or_404(Clinic, pk=pk)
    doctor_list = Doctor.objects.filter(clinic=clinic)
    concurents = Clinic.objects.filter(services__in=clinic.services.all()).exclude(pk=pk).distinct()
    return render(
        request,
        'clinic_detail.html',
        context={'clinic': clinic,
                 'doctor_list': doctor_list,
                 'concurents': concurents}
    )


def doctor_detail(request, pk):
    # Детальная информация о враче
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(
        request,
        'doctor_detail.html',
        context={'doctor': doctor}
    )


def doctors_list(request):
    # Список всех врачей
    doctor_list = Doctor.objects.all()
    return render(
        request,
        'doctor_list.html',
        context={'doctor_list': doctor_list}
    )


def doctors_list_specialization(request):
    specializations = DoctorSpecialization.objects.annotate(Count('doctor')) \
        .filter(doctor__count__gt=0).order_by('-doctor__count')
    return render(
        request,
        'doctors_list_specialization.html',
        context={'specializations': specializations}
    )


def doctors_list_specialization_get(request, pk):
    print('Start')
    doctors = Doctor.objects.filter(specialization__pk=pk)
    specialization = DoctorSpecialization.objects.get(pk=pk)
    return render(
        request,
        'doctors_list_specialization_get.html',
        context={'doctors': doctors,
                 'specialization': specialization}
    )

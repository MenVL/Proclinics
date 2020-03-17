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
    services = ClinicServices.objects.annotate(Count('clinic'))
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


def doctors_list(request):
    # Список всех врачей
    doctor_list = Doctor.objects.all()
    return render(
        request,
        'doctor_list.html',
        context={'doctor_list': doctor_list}
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


def test(request):
    # Тесты работы функций
    clinics_krd = Clinic.objects.filter(city__name='Краснодар')
    clinics_diag = Clinic.objects.filter(services__name='Диагностика')
    clinics_3 = Clinic.objects.filter(services__name__in=['Диагностика', 'Анализы', 'Узи', 'Чистка зубов']).distinct()
    clinics_not_krd = Clinic.objects.exclude(city__name='Краснодар')
    doctors = Doctor.objects.filter(clinic__city__name__iexact='Краснодар')
    dcotors_2 = Doctor.objects.filter(
        clinic__city__name='Краснодар',
        education__icontains='Московский медицинский университет',
        about__icontains='хороший человек'
    )
    # не работает:
    doctors_3 = Doctor.objects.raw('SELECT "catalog_clinic"."name" FROM "catalog_clinic"')
    return render(
        request,
        'test.html',
        context={'clinics_krd': clinics_krd,
                 'clinics_diag': clinics_diag,
                 'clinics_3': clinics_3,
                 'clinics_not_krd': clinics_not_krd,
                 'doctors': doctors,
                 'dcotors_2': dcotors_2,
                 'doctors_3': doctors_3}
    )

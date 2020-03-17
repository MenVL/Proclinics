from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('clinics/', views.clinics_list, name='clinics'),
    path('clinics/<int:pk>/', views.clinic_detail, name='clinic_detail'),
    path('clinics/city/', views.clinics_list_city, name='clinics_city'),
    path('clinics/city/<int:city>', views.clinic_city_detail, name='clinic_city_detail'),
    path('clinics/services/', views.clinic_list_services, name='clinics_services'),
    path('clinics/services/<int:service>', views.clinic_services_detail, name='clinic_services_detail'),
    path('doctors/', views.doctors_list, name='doctors'),
    path('doctors/<int:pk>/', views.doctor_detail, name='doctor_detail'),
    path('doctors/specializations/', views.doctors_list_specialization, name='doctors_specialization'),
    path('doctors/specializations/<int:pk>', views.doctors_list_specialization_get, name='specialization_get'),
]
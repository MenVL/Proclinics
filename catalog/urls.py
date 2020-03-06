from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('clinics/', views.clinics_list, name='clinics'),
    path('clinics/city/', views.clinics_list_city, name='clinics_city'),
    path('clinics/city/<str>:city>/', views.clinics_city_detail, name='clinics_city_detail'),
    path('clinics/<int:pk>/', views.clinic_detail, name='clinic_detail'),
    path('doctors/', views.doctors_list, name='doctors'),
    path('doctors/<int:pk>/', views.doctor_detail, name='doctor_detail'),
]
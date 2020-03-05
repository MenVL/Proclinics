from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    url('clinics/$', views.clinics_list, name='clinics'),
    path('clinics/<int:pk>/', views.clinic_detail, name='clinic_detail'),
    url('doctors/$', views.doctors_list, name='doctors'),
    path('doctors/<int:pk>/', views.doctor_detail, name='doctor_detail'),
]
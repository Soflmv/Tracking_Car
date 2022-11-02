from django.urls import path
from . import views

urlpatterns = [
    path('', views.clear, name='clear'),
    path('car_data_indb', views.car_data_indb, name='car_data_indb'),
    path('pdf_file', views.pdf_file, name='pdf_file'),
]
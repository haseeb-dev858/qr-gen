# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_qr, name='generate_qr'),
    path('',views.download_qr, name='download_qr'),
]

from django.contrib import admin
from django.urls import path


from core.views import index, About, contact, Service

urlpatterns = [
    path('', index, name='home'),
    path('service/', Service, name='service'),
    path('about/', About, name='about'),
    path('contact/', contact, name='contact'),
]


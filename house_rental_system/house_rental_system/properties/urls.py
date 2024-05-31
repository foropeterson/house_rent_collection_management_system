# urls.py
from django.contrib import admin
from django.urls import path
from properties import views
from .views import property_detail

urlpatterns = [
  
    path('', views.home, name='home'),
    path('properties/', views.property_list, name='property_list'),
    path('properties/post/', views.post_property, name='post_property'),
    path('properties/<int:property_id>/', property_detail, name='property_detail'),
    path('news/', views.news_list, name='news_list'),
    path('tenant/', views.tenant_portal, name='tenant_portal'),
    path('landlord/', views.landlord_portal, name='landlord_portal'),
    path('contact/', views.contact_us, name='contact_us'),  # Define the contact_us URL
    path('about/', views.about_us, name='about_us'),
    path('mpesa/confirmation/', views.mpesa_confirmation, name='mpesa_confirmation'),
    path('mpesa/validation/', views.mpesa_validation, name='mpesa_validation'),
]

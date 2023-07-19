from django.urls import path
from . import views

urlpatterns = [
    path('about_company', views.about_company),
    path('contacts', views.contacts),
    path('processing_of_personal_data', views.processing_of_personal_data),
]

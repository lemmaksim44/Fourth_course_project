from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('pass_error/', views.pass_error),
    path('access_is_denied/', views.access_is_denied),
]

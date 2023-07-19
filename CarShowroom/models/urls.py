from django.urls import path
from . import views

urlpatterns = [
    path('<brand_name>', views.models),
    path('<brand_name>/<model_name>', views.about_models),
]

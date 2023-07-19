from django.urls import path
from . import views

urlpatterns = [
    path('osago_calculator', views.osago_calculator),
    path('service_registration', views.service_registration),
    path('test-drive', views.test_drive),
    path('operating_tips', views.operating_tips),
    path('operating_tips/<article_number>', views.article),
    path('guarantee', views.guarantee),
]

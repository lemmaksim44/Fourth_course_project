from django.urls import path
from . import views

urlpatterns = [
    path('used', views.auto_used),
    path('used/filter/brand/<meaning>', views.auto_used_filter_brand),
    path('used/filter/body/<meaning>', views.auto_used_filter_body),
    path('used/<id_car>', views.auto_descriptions),
    path('new', views.auto_new),
    path('new/filter/brand/<meaning>', views.auto_new_filter_brand),
    path('new/filter/body/<meaning>', views.auto_new_filter_body),
    path('new/<id_car>', views.auto_descriptions),
]

from django.shortcuts import render
from .models import Brand, Model, Modification,Car_equipment, Model_picture


def models(request, brand_name):
    brand = Brand.objects.all().order_by('name')
    car_class = Model.objects.raw('SELECT id_model, id_brand_id, id_class_id FROM models_model GROUP BY id_brand_id, id_class_id')
    selected_brand = Brand.objects.get(name = brand_name)
    model = Model.objects.order_by('name').filter(id_brand = selected_brand.id_brand)
    car_equipment = Car_equipment.objects.raw('SELECT id_car_equipment, id_model_id, MIN(price) AS price FROM models_car_equipment GROUP BY id_model_id')
    return render(request, 'models/models.html', {'brand': brand, 'car_class': car_class, 'model': model, 'car_equipment': car_equipment, 'selected_brand': selected_brand})


def about_models(request, brand_name, model_name):
    brand = Brand.objects.all().order_by('name')
    selected_brand = Brand.objects.get(name = brand_name)
    model = Model.objects.get(name = model_name)
    modification = Modification.objects.order_by('engine_power').filter(id_model = model.id_model)
    model_picture = Model_picture.objects.get(id_model = model.id_model)
    car_equipment = Car_equipment.objects.order_by('price').filter(id_model = model.id_model)
    car_equipment_reverse = Car_equipment.objects.order_by('-price').filter(id_model = model.id_model)
    return render(request, 'models/about_models.html', {'selected_brand': selected_brand, 'model': model, 'modification': modification,'model_picture': model_picture, 'car_equipment': car_equipment, 'brand': brand, 'car_equipment_reverse': car_equipment_reverse})
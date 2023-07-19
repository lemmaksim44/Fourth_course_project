from django.shortcuts import render
from models.models import Brand
from stock.models import Car_in_stock
from services.models import Operating_tips


def main(request):
    brand = Brand.objects.all().order_by('name')
    car_in_stock = Car_in_stock.objects.all()[:6]
    operating_tips = Operating_tips.objects.all()[:4]
    return render(request, 'main/main_page.html', {'brand': brand, 'car_in_stock': car_in_stock, 'operating_tips': operating_tips})


def pass_error(request):
    return render(request, 'main/pass_error.html')


def access_is_denied(request):
    return render(request, 'main/access_is_denied.html')
from django.shortcuts import render
from django.http import HttpResponseRedirect
from models.models import Brand
from .models import *
from company.forms import *


def auto_used(request):
    brand = Brand.objects.all().order_by('name')
    car_in_stock = Car_in_stock.objects.order_by('price').filter(used = True)
    car_brand = Car_in_stock.objects.raw('SELECT id_car_in_stock, brand FROM stock_car_in_stock WHERE used = True GROUP BY brand')
    body_type = Car_in_stock.objects.raw('SELECT id_car_in_stock, stock_body_type.name FROM stock_car_in_stock LEFT JOIN stock_body_type ON id_body_type_id = id_body_type WHERE used = True GROUP BY id_body_type_id')
    return render(request, 'stock/auto_used.html', {'brand': brand, 'car_in_stock': car_in_stock, 'body_type': body_type, 'car_brand': car_brand})


def auto_used_filter_brand(request, meaning):
    brand = Brand.objects.all().order_by('name')
    car_in_stock = Car_in_stock.objects.order_by('price').filter(used = True, brand = meaning)
    car_brand = Car_in_stock.objects.raw('SELECT id_car_in_stock, brand FROM stock_car_in_stock WHERE used = True GROUP BY brand')
    body_type = Car_in_stock.objects.raw('SELECT id_car_in_stock, stock_body_type.name FROM stock_car_in_stock LEFT JOIN stock_body_type ON id_body_type_id = id_body_type WHERE used = True GROUP BY id_body_type_id')
    return render(request, 'stock/auto_used.html', {'brand': brand, 'car_in_stock': car_in_stock, 'body_type': body_type, 'car_brand': car_brand})


def auto_used_filter_body(request, meaning):
    brand = Brand.objects.all().order_by('name')
    car_in_stock = Car_in_stock.objects.order_by('price').filter(used = True, id_body_type = meaning)
    car_brand = Car_in_stock.objects.raw('SELECT id_car_in_stock, brand FROM stock_car_in_stock WHERE used = True GROUP BY brand')
    body_type = Car_in_stock.objects.raw('SELECT id_car_in_stock, stock_body_type.name FROM stock_car_in_stock LEFT JOIN stock_body_type ON id_body_type_id = id_body_type WHERE used = True GROUP BY id_body_type_id')
    return render(request, 'stock/auto_used.html', {'brand': brand, 'car_in_stock': car_in_stock, 'body_type': body_type, 'car_brand': car_brand})


def auto_new(request):
    brand = Brand.objects.all().order_by('name')
    car_in_stock = Car_in_stock.objects.order_by('price').filter(used = False)
    car_brand = Car_in_stock.objects.raw('SELECT id_car_in_stock, brand FROM stock_car_in_stock WHERE used = False GROUP BY brand')
    body_type = Car_in_stock.objects.raw('SELECT id_car_in_stock, stock_body_type.name FROM stock_car_in_stock LEFT JOIN stock_body_type ON id_body_type_id = id_body_type WHERE used = False GROUP BY id_body_type_id')
    return render(request, 'stock/auto_new.html', {'brand': brand, 'car_in_stock': car_in_stock, 'body_type': body_type, 'car_brand': car_brand})


def auto_new_filter_brand(request, meaning):
    brand = Brand.objects.all().order_by('name')
    car_in_stock = Car_in_stock.objects.order_by('price').filter(used = False, brand = meaning)
    car_brand = Car_in_stock.objects.raw('SELECT id_car_in_stock, brand FROM stock_car_in_stock WHERE used = False GROUP BY brand')
    body_type = Car_in_stock.objects.raw('SELECT id_car_in_stock, stock_body_type.name FROM stock_car_in_stock LEFT JOIN stock_body_type ON id_body_type_id = id_body_type WHERE used = False GROUP BY id_body_type_id')
    return render(request, 'stock/auto_new.html', {'brand': brand, 'car_in_stock': car_in_stock, 'body_type': body_type, 'car_brand': car_brand})


def auto_new_filter_body(request, meaning):
    brand = Brand.objects.all().order_by('name')
    car_in_stock = Car_in_stock.objects.order_by('price').filter(used = False, id_body_type = meaning)
    car_brand = Car_in_stock.objects.raw('SELECT id_car_in_stock, brand FROM stock_car_in_stock WHERE used = False GROUP BY brand')
    body_type = Car_in_stock.objects.raw('SELECT id_car_in_stock, stock_body_type.name FROM stock_car_in_stock LEFT JOIN stock_body_type ON id_body_type_id = id_body_type WHERE used = False GROUP BY id_body_type_id')
    return render(request, 'stock/auto_new.html', {'brand': brand, 'car_in_stock': car_in_stock, 'body_type': body_type, 'car_brand': car_brand})


def auto_descriptions(request, id_car):
    brand = Brand.objects.all().order_by('name')
    car_in_stock = Car_in_stock.objects.get(id_car_in_stock = id_car)
    car_picture = Car_picture.objects.filter(id_car_in_stock = id_car)
    client = Client.objects.all()
    form = RequestForm()
    form_client = ClientForm()

    error = ''
    if request.method =='POST':
        form = RequestForm(request.POST)
        form_client = ClientForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            
            if len(str(post.client_name)) <= 200 and len(post.client_phone) == 11 and (str(post.client_phone).find('7') == 0 or str(post.client_phone).find('8') == 0):
                
                if post.client_email == None or (str(post.client_email).find('@') != -1 and str(post.client_email).find('.') != -1 and str(post.client_email).find(' ') == -1):
                    
                    check = False
                    for line in client:
                        if line.client_phone == post.client_phone:
                            check = True
                    
                    if check == False:
                        form_client.save()

                    post.save()
                    if car_in_stock.used:
                        return HttpResponseRedirect('/stock/used/' + id_car)
                    else:
                        return HttpResponseRedirect('/stock/new/' + id_car)
                
                else:
                    error = 'Ошибка заполнения формы'
            else:
                error = 'Ошибка заполнения формы'
        else:
            error = 'Ошибка заполнения формы'

    return render(request, 'stock/auto_descriptions.html', {'brand': brand, 'car_in_stock': car_in_stock, 'car_picture': car_picture, 'form': form, 'error': error, 'form_client': form_client})
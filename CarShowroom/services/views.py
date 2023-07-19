from django.shortcuts import render
from django.http import HttpResponseRedirect
from models.models import Brand, Model
from .models import *
from company.forms import *
from datetime import datetime


def osago_calculator(request):
    brand = Brand.objects.all().order_by('name')
    region = Region.objects.all().order_by('name')
    city = City.objects.all().order_by('id_city')
    client = Client.objects.all()
    form =RequestForm()
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
                    return HttpResponseRedirect('/services/osago_calculator')
                
                else:
                    error = 'Ошибка заполнения формы'
            else:
                error = 'Ошибка заполнения формы'
        else:
            error = 'Ошибка заполнения формы'
    
    return render(request, 'services/osago_calculator.html', {'brand': brand, 'form': form, 'form_client': form_client, 'error': error, 'region': region, 'city': city})


def service_registration(request):
    brand = Brand.objects.all().order_by('name')
    client = Client.objects.all()
    form =RequestForm()
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
                    return HttpResponseRedirect('/services/service_registration')
                
                else:
                    error = 'Ошибка заполнения формы'
            else:
                error = 'Ошибка заполнения формы'
        else:
            error = 'Ошибка заполнения формы'

    return render(request, 'services/service_registration.html', {'brand': brand, 'form': form, 'form_client': form_client, 'error': error})


def test_drive(request):
    brand = Brand.objects.all().order_by('name')
    model = Model.objects.all().order_by('name')
    tomorrow_date = datetime.now().date()
    week = datetime.now().date()
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

                    if len(str(post.comment).split()) >= 2:
                    
                        check = False
                        for line in client:
                            if line.client_phone == post.client_phone:
                                check = True
                    
                        if check == False:
                            form_client.save()

                        post.save()
                        return HttpResponseRedirect('/services/test-drive')
                    
                    else:
                        error = 'Ошибка заполнения формы'
                else:
                    error = 'Ошибка заполнения формы'
            else:
                error = 'Ошибка заполнения формы'
        else:
            error = 'Ошибка заполнения формы'

    return render(request, 'services/test_drive.html', {'brand': brand, 'model': model, 'form': form, 'form_client': form_client, 'error': error, 'tomorrow_date': tomorrow_date, 'week': week})


def operating_tips(request):
    brand = Brand.objects.all().order_by('name')
    tips = Operating_tips.objects.order_by('title').all()
    return render(request, 'services/operating_tips.html', {'brand': brand, 'tips': tips})


def article(request, article_number):
    brand = Brand.objects.all().order_by('name')
    tips = Operating_tips.objects.order_by('title').all()
    tip = Operating_tips.objects.get(id_operating_tips = article_number)
    return render(request, 'services/article.html', {'brand': brand, 'tips': tips, 'tip': tip})


def guarantee(request):
    brand = Brand.objects.all().order_by('name')
    return render(request, 'services/guarantee.html', {'brand': brand})
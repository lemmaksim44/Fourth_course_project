from django.shortcuts import render
from django.http import HttpResponseRedirect
from models.models import Brand
from .forms import *


def about_company(request):
    brand = Brand.objects.all().order_by('name')
    return render(request, 'company/about_company.html', {'brand': brand})


def contacts(request):

    brand = Brand.objects.all().order_by('name')
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
                    return HttpResponseRedirect('/company/contacts')
                
                else:
                    error = 'Ошибка заполнения формы'
            else:
                error = 'Ошибка заполнения формы'
        else:
            error = 'Ошибка заполнения формы'

    return render(request, 'company/contacts.html', {'brand': brand, 'form': form, 'error': error, 'form_client': form_client})


def processing_of_personal_data(request):
    brand = Brand.objects.all().order_by('name')
    return render(request, 'company/processing_of_personal_data.html', {'brand': brand})

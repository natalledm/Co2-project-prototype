from django.http import HttpResponse, HttpResponseRedirect
from .models import Cars, BrandForm
from django.template import loader
from django.shortcuts import render

def show_car(request, id):
        car = Cars.objects.get(id=id)
        context = {'car': car}
        return render(request, 'cars/single_car.html', context)

def show_form(request):
        context = {}
        return render(request, 'cars/index.html', context)

def get_brand(request):
        car = request.GET.get('car')
        brand = car.upper() # because our data is all in uppercase
        cars = Cars.objects.filter(brand__startswith=brand)
        context = {'cars_list': cars}
        return render(request, 'cars/search.html', context)
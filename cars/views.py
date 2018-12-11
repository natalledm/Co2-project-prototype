from django.http import HttpResponse, JsonResponse
from .models import Cars
from django.template import loader
from django.shortcuts import render

def home(request):
        return HttpResponse('This is where the search box will be.')

# def filterByBrand(request, brand):
#         results = []
#         brand = brand.upper() # because our data is all in uppercase
#         for car in Cars.objects.filter(brand__startswith=brand):
#                 json_dict = dict()
#                 for field in car._meta.fields:
#                         json_dict[field.name] = getattr(car, field.name)
#                 results.append(json_dict)
#         response = JsonResponse({'results': results})

#         return HttpResponse(response.content)

# def filterByBrand(request, brand):
#         results = []
#         brand = brand.upper() # because our data is all in uppercase
#         cars = Cars.objects.filter(brand__startswith=brand)
#         # for car in Cars.objects.filter(brand__startswith=brand):
#         #         car_dict = dict()
#         #         for field in car._meta.fields:
#         #                 car_dict[field.name] = getattr(car, field.name)
#         #         results.append(car_dict)
#         # response = JsonResponse({'results': results})
#         # return HttpResponse(template.render(results.content))
#         context = {'cars_list': cars}

        # { context: { results: [ { model: abc, brand: def, ... }, {  }, ... ] }
        # return render(request, 'cars/search.html', context)

def filterByBrand(request, brand):
        brand = brand.upper() # because our data is all in uppercase
        cars = Cars.objects.filter(brand__startswith=brand)
        context = {'cars_list': cars}
        return render(request, 'cars/search.html', context)

def show_car(request, id):
        car = Cars.objects.get(id=id)
        context = {'car': car}
        return render(request, 'cars/single_car.html', context)
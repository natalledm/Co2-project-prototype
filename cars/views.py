from django.http import HttpResponse, JsonResponse
from .models import Cars

def home(request):
    return HttpResponse('Hello, world!')

def filterByBrand(request, brand):
    json_dict = dict()
    for car in Cars.objects.filter(brand__startswith=brand):
        for field in car._meta.fields:
            json_dict[field.name] = getattr(car, field.name)
    response = JsonResponse(json_dict)
    return HttpResponse(response.content)
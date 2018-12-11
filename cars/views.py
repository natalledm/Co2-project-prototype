from django.http import HttpResponse, JsonResponse
from .models import Cars

def home(request):
        return HttpResponse('Hello, world!')

def filterByBrand(request, brand):
        results = []
        brand = brand.upper() # because our data is all in uppercase
        for car in Cars.objects.filter(brand__startswith=brand):
                json_dict = dict()
                for field in car._meta.fields:
                        json_dict[field.name] = getattr(car, field.name)
                results.append(json_dict)
        response = JsonResponse({'results': results})

        return HttpResponse(response.content)
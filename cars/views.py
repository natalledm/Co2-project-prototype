from django.http import HttpResponse
from .models import Cars

def home(request):
    return HttpResponse('Hello, world!')

def filterByBrand(request, brand):
    return Cars.objects.filter(brand__startswith=brand)[:4]
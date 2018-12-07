from django.urls import path
from . import views

app_name = 'cars'
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:brand>/', views.filterByBrand, name='brand'),
]
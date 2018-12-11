from django.urls import path
from . import views

app_name = 'cars'
urlpatterns = [
    path('', views.home, name='home'),
    path('search/<str:brand>/', views.filterByBrand, name='brand'),
    path('<int:id>/', views.show_car, name='unique_car')
]
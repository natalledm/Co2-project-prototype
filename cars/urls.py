from django.urls import path
from . import views

app_name = 'cars'
urlpatterns = [
    path('search/', views.get_brand, name='brand'),
    path('<int:id>/', views.show_car, name='unique_car')
]
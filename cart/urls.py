from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/add/', views.add, name='cart.add'),
    path('purchase/', views.purchase, name='cart.purchase'),
]

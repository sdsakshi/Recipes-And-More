from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('photo/<str:pk>/', views.viewFood, name='food'),
    path('add/', views.addFood, name='add'),
]
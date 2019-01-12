from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data/', views.data_presentation, name='data_presenation'),
    path('cognitive/', views.cognitive, name='cognitive')
]
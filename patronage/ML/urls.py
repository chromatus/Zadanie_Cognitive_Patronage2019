from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data/', views.data_table, name='data_table'),
    path('cognitive/', views.cognitive, name='cognitive'),
    path('data/form', views.form, name='data_form'),
    path('data/filtered', views.data_filtered, name='filtered'),    
]
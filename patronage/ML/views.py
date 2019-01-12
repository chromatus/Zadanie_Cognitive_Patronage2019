from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .cognitive import Cognitive
# Create your views here.



def index(request):
    template = loader.get_template('ML/index.html')
    return HttpResponse(template.render())

def data_presentation(request):
    response = "You're looking at the placeholder for data presentations page."
    return HttpResponse(response)

def cognitive(request):
    cognitive = Cognitive()
    cognitive.data_import_from_file()
    cognitive.data_preprocessing()
    cognitive.data_predicting()
    cognitive.data_rescaling()
    cognitive.data_export()
    response = "Data has been loaded"
    return HttpResponse(response)
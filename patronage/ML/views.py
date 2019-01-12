from django.template import loader
from django.http import HttpResponse

from .cognitive import Cognitive
from .models import Salary


def index(request):
    template = loader.get_template('ML/index.html')
    return HttpResponse(template.render())

def data_table(request):
    template = loader.get_template('ML/display.html')
    salary_list = Salary.objects.order_by('id')
    context = {'salary_list' : salary_list}
    return HttpResponse(template.render(context, request))

def cognitive(request):
    cognitive = Cognitive()
    cognitive.data_import_from_file()
    cognitive.data_preprocessing()
    cognitive.data_predicting()
    cognitive.data_rescaling()
    cognitive.data_export()
    response = "Data has been loaded"
    return HttpResponse(response)

def plots(request):
    return HttpResponse()
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse

from .cognitive import Cognitive
from .models import Salary
from django.http.response import HttpResponseRedirect


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

def form(request):
    template = loader.get_template('ML/form.html')
    salary_list = Salary.objects.order_by('id')
    context = {'salary_list' : salary_list}
    return HttpResponse(template.render(context, request))

def data_filtered(request):
    salary_list = Salary.objects.order_by('id')
    if request.POST['max_salary'] != '':
        salary_list = salary_list.exclude(salary__gt=request.POST['max_salary'])
    if request.POST['min_salary'] != '':
        salary_list = salary_list.filter(salary__gte=request.POST['min_salary'])
    if request.POST['max_years'] != '':
        salary_list = salary_list.exclude(years_worked__gt=request.POST['max_years'])
    if request.POST['min_years'] != '':
        salary_list = salary_list.filter(years_worked__gte=request.POST['min_years'])
    context = {'salary_list' : salary_list}
    template = loader.get_template('ML/display.html')
    return HttpResponse(template.render(context, request))
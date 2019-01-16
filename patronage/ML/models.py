from django.db import models

# Create your models here.

class Salary(models.Model):
    years_worked = models.FloatField()
    salary = models.FloatField()
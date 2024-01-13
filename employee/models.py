from django.db import models

# Create your models here.

class Employee(models.Model):
    empID = models.CharField(max_length = 100)
    empName = models.CharField(max_length = 50)
    empEmail = models.CharField(max_length = 50)
    empAddress = models.CharField(max_length = 50)
    empPhone = models.CharField(max_length = 50)
from django.db import models

# Create your models here.
class empdtls(models.Model):
    empid=models.IntegerField()
    empname=models.CharField(max_length=30)
    doj=models.CharField(max_length=20)
    expsalary=models.IntegerField()
    prevexp=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)


class log(models.Model):
    user=models.CharField(max_length=30)
    pwd=models.CharField(max_length=30)
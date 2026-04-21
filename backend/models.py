from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100,null=True)
    gender=models.CharField(max_length=30,null=True)
    course=models.CharField(max_length=50,null=True)
    city=models.CharField(max_length=50,null=True)

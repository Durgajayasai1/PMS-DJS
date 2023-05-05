from django.db import models
from datetime import *

# Create your models here

class User_Details(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)  
class Project_Details(models.Model):
    id=models.AutoField(primary_key=True)
    project=models.CharField(max_length=100,null=True)
    type=models.CharField(max_length=100,null=True)
    start=models.DateField(null=True)
    end=models.DateField(null=True)
    priority=models.CharField(max_length=100,null=True)
    description=models.CharField(max_length=1000,null=True)
class contact_us(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    description=models.CharField(max_length=1000,null=True)
class todo1(models.Model):
    id=models.AutoField(primary_key=True)
    idx=models.IntegerField(null=True)
    task=models.CharField(max_length=100,null=True)

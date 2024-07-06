from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class CarTable(models.Model):
    cname=models.CharField(max_length=20)
    cimage=models.ImageField(upload_to='image/')
    
    

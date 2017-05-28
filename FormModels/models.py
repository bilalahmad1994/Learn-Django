from django.db import models

# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=234)
    last_name=models.CharField(max_length=234)
    email=models.CharField(max_length=234,unique=True)

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Student(AbstractUser):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=255, unique=True)
    password=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    age=models.IntegerField()
from pyexpat import model
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    isActive = models.BooleanField(default=False)

class Teacher (models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    isActive = models.BooleanField(default=False)
    subject = models.CharField(max_length = 100)
    



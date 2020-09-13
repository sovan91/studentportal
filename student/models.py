from django.db import models


# Create your models here.
class Student(models.Model):
    No = models.IntegerField()
    Name = models.CharField(max_length=200)
    Age = models.IntegerField()
    Mob = models.CharField(max_length=20)
    Add = models.CharField(max_length=200)

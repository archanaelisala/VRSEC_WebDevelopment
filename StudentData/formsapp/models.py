from django.db import models

# Create your models here.
class Student(models.Model):
	college_name = models.CharField(max_length=40)
	Details = models.CharField(max_length=100)

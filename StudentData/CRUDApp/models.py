from django.db import models

# Create your models here.
class Studentdata(models.Model):
	Firstname = models.CharField(max_length=30)
	Lastname = models.CharField(max_length=30)
	Username = models.CharField(max_length=60)
	Password = models.CharField(max_length=30)
	Email = models.EmailField(max_length=100)
	Mobile = models.IntegerField(null=True)
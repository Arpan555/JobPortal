from django.db import models

# Create your models here.
class Indorejob(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=50)
    email=models.EmailField()
    phonenumber=models.IntegerField()
class Punejob(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=50)
    email=models.EmailField()
    phonenumber=models.IntegerField()
class Banglorejob(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=50)
    email=models.EmailField()
    phonenumber=models.IntegerField()

class Hyderabadjob(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=50)
    email=models.EmailField()
    phonenumber=models.IntegerField()

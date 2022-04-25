from django.db import models
from django.contrib import admin
from django import forms



# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return self.first_name
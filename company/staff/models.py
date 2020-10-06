# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Employee(models.Model):
	Employee_name=models.CharField(max_length=30)
	Department=models.CharField(max_length=30)
	Email=models.EmailField()
	Dateofbirth=models.DateField()
	Picture=models.ImageField(upload_to='staff/media/images', blank=True)
	def __str__(self):
		return self.Employee_name
class Department(models.Model):
	Department_name=models.CharField(max_length=30)
	manager=models.ForeignKey(Employee, related_name='employees', blank=True)

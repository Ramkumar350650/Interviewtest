# Interviewtest
completed test all result done

Python Questions :

1.Ans:

sum_of_multiples = 0

for i in range(1, 1000):
	if (i % 3) == 0 or (i % 5) == 0:
		
		sum_of_multiples += i

print( sum_of_multiples)


2.Ans:

prev, cur = 0, 1
total = 0
while True:
    prev, cur = cur, prev + cur
    if cur >= 4000000:
        break
    if cur % 2 == 0:
        total += cur
print(total)



Django Questions:
1.Ans:
Django-admin startproject company
cd company
python manage.py startapp staff


2.Ans:
models.py
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
  
3.Ans:
admin.py:
from __future__ import unicode_literals

from django.contrib import admin

from staff.models import *

class DepartmentInline(admin.TabularInline):
    model = Department
    fields = ['Department_name','manager',]    

class EmployeeAdmin(admin.ModelAdmin):
    list_display =('Employee_name','Department','Email','Dateofbirth','Picture')
    list_filter = ['Department','Dateofbirth']
    inlines = [DepartmentInline]

class DepartmentAdmin(admin.ModelAdmin):
	list_display =('Department_name','manager')


# Register your models here.
admin.site.register(Employee,EmployeeloyeeAdmin)
admin.site.register(Department,DepartmentAdmin)  


4.Ans:
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

note:already created superuser:
username:ramkumar
paswword:Ramkumar123






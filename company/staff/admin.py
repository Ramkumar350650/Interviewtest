# -*- coding: utf-8 -*-
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
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Department,DepartmentAdmin)

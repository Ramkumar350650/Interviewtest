# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from staff.models import *
from staff.forms import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView

# Create your views here.
class DepartmentListView(ListView):
	context_object_name = 'Departments'
	model=Department
	template_name = 'staff/department.html'

class DepartmentDetailView(DetailView):
	context_object_name = 'Departments'
	model=Department
	template_name = 'staff/department.html'



class EmployeeListView(ListView):
	context_object_name = 'Employees'
	model=Employee
	template_name = 'staff/employee.html'

class EmployeeDetailView(DetailView):
	context_object_name = 'Employees'
	model=Employee
	template_name = 'staff/employee.html'


class EmployeeCreateView(CreateView):

	model=Employee
	template_name = 'staff/employee.html'

class EmployeeUpdateView(UpdateView):
	model=Employee
	template_name = 'staff/employee.html'


def insert_view(request):
	form=EmployeeForm()
	if request.method=='POST':
		form=EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')
	return render(request,'staff/EmployeeForm.html',{'form':form})


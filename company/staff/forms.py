from django import forms

from staff.models import *

class EmployeeForm(forms.ModelForm):
	class Meta:
		model=Employee
		fields=['Employee_name','Department']

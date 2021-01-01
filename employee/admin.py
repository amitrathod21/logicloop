from django.contrib import admin
from employee.models import Employee

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','done']


admin.site.register(Employee,EmployeeAdmin)
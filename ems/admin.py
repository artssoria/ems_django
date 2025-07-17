from django.contrib import admin

from .models import Employee, Job

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'joining_date','phone_number','show_jobs']
    def show_jobs(self, obj):
        return ", ".join([j.name for j in obj.jobs.all()])
    show_jobs.short_description = "Trabajos"
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['name']
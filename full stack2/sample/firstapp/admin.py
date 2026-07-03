from django.contrib import admin
from .models import Department, Course, Student


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'credits', 'department']
    search_fields = ['name']
    list_filter = ['department']


admin.site.register(Department)
admin.site.register(Student)
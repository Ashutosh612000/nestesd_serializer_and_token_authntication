from django.contrib import admin
from .models import Instructor,Course

class InstructorAdmin(admin.ModelAdmin):
    list_display = ['name','email']

class CoursesAdmin(admin.ModelAdmin):
    list_display = ['titel','rating','instructor']

admin.site.register(Course, CoursesAdmin)
admin.site.register(Instructor,InstructorAdmin)   

# Register your models here.

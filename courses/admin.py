from django.contrib import admin

from .models import Teacher, Course, HomeWork

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Names',               {'fields': ['name']}),
        ('Last Names', {'fields': ['patern_name', 'matern_name']}),
    ]
admin.site.register(Teacher, TeacherAdmin)

class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Teacher',               {'fields': ['teacher']}),
        ('Course', {'fields': ['course_name','descripton']}),
    ]
admin.site.register(Course, CourseAdmin)

class HomeWorkAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Course',               {'fields': ['course']}),
        ('HomeWork', {'fields': ['homework_name', 'description']}),
        ('Date Informations', {'fields': ['return_date']}),
    ]
admin.site.register(HomeWork, HomeWorkAdmin)
from django.contrib import admin

from .models import Teacher, Course, HomeWork

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'patern_name', 'matern_name')
    fieldsets = [
        ('Names',               {'fields': ['name']}),
        ('Last Names', {'fields': ['patern_name', 'matern_name']}),
    ]
admin.site.register(Teacher, TeacherAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','teacher', 'course_name', 'description')
    fieldsets = [
        ('Teacher',               {'fields': ['teacher']}),
        ('Course', {'fields': ['course_name','description']}),
    ]
admin.site.register(Course, CourseAdmin)

class HomeWorkAdmin(admin.ModelAdmin):
    list_display = ('id','course', 'homework_name', 'description', 'return_date')
    list_filter = ['return_date', 'course']
    fieldsets = [
        ('Course',               {'fields': ['course']}),
        ('HomeWork', {'fields': ['homework_name', 'description']}),
        ('Date Informations', {'fields': ['return_date']}),
    ]
admin.site.register(HomeWork, HomeWorkAdmin)
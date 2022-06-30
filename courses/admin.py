from django.contrib import admin

from courses.models import Teacher
from .models import Teacher, Course, HomeWork

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(HomeWork)
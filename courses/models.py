from time import time
from django.db import models
from django.utils import timezone
# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    patern_name = models.CharField(max_length=20)
    matern_name = models.CharField(max_length=20)

    def __str__(self):
        return self.name + ' ' + self.patern_name + ' ' + self.matern_name

class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.course_name

class HomeWork(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    homework_name = models.CharField(max_length=100)
    description = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()

    def __str__(self):
        return f'{self.course} {self.homework_name} - Return Date: {self.return_date}'

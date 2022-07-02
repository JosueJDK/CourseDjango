from django.forms import ModelForm
from .models import Course, Teacher

class FormTeacher(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class FormCourse(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
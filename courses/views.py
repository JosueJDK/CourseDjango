from django.shortcuts import render, get_object_or_404
from .models import Course
# Create your views here.
def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses' : courses})

def course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course.html', {'course' : course})
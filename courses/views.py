from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Course, HomeWork, Teacher
from .forms import FormCourse, FormTeacher

# Create your views here.
def home(request):
    return render(request, 'home.html')

def teacher(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher.html', {'teachers': teachers})

def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses' : courses})

def course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course.html', {'course' : course})

def homeworks(request):
    homeworks = HomeWork.objects.all()
    return render(request, 'homeworks.html', {'homeworks' : homeworks})

def form_teacher(request):
    form = FormTeacher()
    if request.method == 'POST':
        form = FormTeacher(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:teacher')
    context = {'form': form}

    return render(request, 'form_teacher.html', context)

def delete_teacher(request, pk):
    teacher = Teacher.objects.get(id = pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('courses:teacher')
    return render(request, 'delete_teacher.html', {'obj':teacher})


def form_course(request):
    form = FormCourse()

    if request.method == 'POST':
        form = FormCourse(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:courses')
    context = {'form':form}
    return render(request, 'form_course.html', context)

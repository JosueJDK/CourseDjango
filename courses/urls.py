from django.urls import path
from .views import delete_teacher, form_course, home, teacher, courses, course, form_teacher, teacher, homeworks
app_name = 'courses'

urlpatterns = [
    path('', home, name='home'),
    path('teacher/', teacher, name='teacher'),
    path('teacher/create-teacher/', form_teacher, name='create-teacher'),
    path('teacher/delete-teacher/<int:pk>', delete_teacher, name='delete-teacher'),
    path('courses/' , courses, name='courses'),
    path('courses/course/<int:course_id>/' , course, name='course'),
    path('course/create-course/', form_course, name='create-course'),
    path('homeworks' , homeworks, name='homeworks'),
]


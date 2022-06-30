from django.urls import path
from .views import courses, course
app_name = 'courses'

urlpatterns = [
    path('courses/' , courses, name='courses'),
    path('courses/course/<int:course_id>/' , course, name='course'),
]

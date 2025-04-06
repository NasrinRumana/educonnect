from django.shortcuts import render, get_object_or_404
from .models import Course

def course_list(request):
    # Fetch all courses from the database
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    # Fetch a specific course using the course_id or return a 404 if not found
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})
from django.shortcuts import render

def home(request):
    # Add your home view logic here
    return render(request, 'home.html')  # You can change this to the correct template


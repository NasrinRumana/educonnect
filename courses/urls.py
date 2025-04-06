from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),  # List of all courses
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),  # Details of a specific course
]

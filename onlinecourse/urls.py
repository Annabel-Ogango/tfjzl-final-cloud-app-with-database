from django.urls import path
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # Home page listing all courses (using Class-Based View)
    path('', views.CourseListView.as_view(), name='index'),

    # Course details (using Class-Based View)
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),

    # Enrollment path (Functional View)
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),

    # Task 5 & 6: Exam submission and results (Functional Views)
    path('<int:course_id>/submit/', views.submit, name='submit'),
    path('course/<int:course_id>/submission/<int:submission_id>/result/', 
         views.show_exam_result, name='exam_result'),
]
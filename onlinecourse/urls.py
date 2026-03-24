from django.urls import path
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # ... your existing paths (e.g., '', 'course/<int:pk>/', etc.) ...
    
    # Path for submit view
    path('<int:course_id>/submit/', views.submit, name='submit'),
    
    # Path for exam result view
    path('course/<int:course_id>/submission/<int:submission_id>/result/', 
         views.show_exam_result, name='exam_result'),
]
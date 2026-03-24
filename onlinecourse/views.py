from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission, Enrollment

# Helper function to extract answers from POST data
def extract_answers(request):
    choice_ids = []
    for key, value in request.POST.items():
        if key.startswith('choice_'):
            choice_ids.append(int(value))
    return Choice.objects.filter(id__in=choice_ids)

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    user = request.user
    # Get the enrollment for the current user and course
    enrollment = Enrollment.objects.get(user=user, course=course)
    # Create a new submission
    submission = Submission.objects.create(enrollment=enrollment)
    # Extract and set the choices
    choices = extract_answers(request)
    submission.choices.set(choices)
    
    return HttpResponseRedirect(reverse(viewname='onlinecourse:exam_result', 
                                        args=(course.id, submission.id)))

def show_exam_result(request, course_id, submission_id):
    context = {}
    course = get_object_or_404(Course, pk=course_id)
    submission = Submission.objects.get(id=submission_id)
    choices = submission.choices.all()

    total_score = 0
    questions = course.question_set.all()

    for question in questions:
        # Get all correct choices for this specific question
        correct_choices = question.choice_set.filter(is_correct=True)
        # Get user's selected choices for this specific question
        selected_choices = choices.filter(question=question)

        # Check if the sets match exactly
        if set(correct_choices) == set(selected_choices):
            total_score += question.grade

    context['course'] = course
    context['grade'] = total_score
    context['choices'] = choices
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
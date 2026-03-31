from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models

def index(request):
    questions = models.Question.objects.all()
    context = {'latest_question_list': questions} 
    return render(request, 'hypothetical/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    return render(request, 'hypothetical/detail', {'question': question})

def results(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    return render(request, 'hypothetical/results', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    return render(request, 'hypothetical/vote', {'question': question})


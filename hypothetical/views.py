from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Question, Vote
from django.urls import reverse

def index(request):
    questions = Question.objects.all()
    context = {'latest_question_list': questions} 
    return render(request, 'hypothetical/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'hypothetical/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'hypothetical/results', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = Question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist): 
        return render(request,
               "hypothetical/detail", 
               {
                   "question": question,
                   "error_message": "You didn't pick a choice sweetie"
               }
        )
    else: 
        Vote.objects.create(choice=selected_choice, voter=selected_choice.author)

    return HttpResponseRedirect(reverse("hypothetical:results", args=(question.id)))


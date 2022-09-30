from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Quiz
# Create your views here.
# 
# home(response):
#     quizes = Quiz.objects.all()
#     return render(response, 'main/list.html', {'quizes': quizes})

class QuizList(ListView):
        model = Quiz
        context_object_name = 'quizlist'
        
class QuizDetail(DetailView):
    model = Quiz
    context_object_name = 'quizdetail'

from django.urls import path

from . import views

urlpatterns = [
     path("", views.QuizList.as_view(), name="quizlist"),
     path("quiz/<int:pk>/", views.QuizDetail.as_view(), name="quizdetails")
]

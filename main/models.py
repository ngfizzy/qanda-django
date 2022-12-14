from django.db import models

# Create your models here.


class Option(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=250)
    options = models.ManyToManyField(Option)
    answer = models.ForeignKey(
        Option, related_name='answer', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Quiz(models.Model):
    name = models.CharField(max_length=250)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name


class QuizQuestionAnswer(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE)

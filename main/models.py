from django.utils import timezone
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Option(models.Model):
    name = models.CharField(max_length=250)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Question(models.Model):
    name = models.CharField(max_length=250)
    options = models.ManyToManyField(Option)
    answer = models.ForeignKey(
        Option, related_name='answer', on_delete=models.CASCADE)
    created = models.DateTimeField( default=timezone.now)
    updated = models.DateTimeField( default=timezone.now)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    name = models.CharField(max_length=250)
    questions = models.ManyToManyField(Question)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class QuizQuestionAnswer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option=models.ForeignKey(Option, on_delete=models.CASCADE)
    created=models.DateTimeField(default=timezone.now)
    updated=models.DateTimeField(default=timezone.now)

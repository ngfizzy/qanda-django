from django.contrib import admin
from .models import Option, Question, Quiz, QuizQuestionAnswer

# Register your models here.
admin.site.register(QuizQuestionAnswer)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)

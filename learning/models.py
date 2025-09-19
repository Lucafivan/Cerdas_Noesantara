from django.db import models
from django.conf import settings
# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)

class Chapter(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

class Material(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    difficulty_group = models.CharField(max_length=10,
        choices=[('fast','Fast'),('mid','Mid'),('slow','Slow')])
    content = models.TextField()

class Quiz(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.TextField()
    choices = models.JSONField()
    answer_key = models.CharField(max_length=100)

class UserQuizResult(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    attempt_no = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
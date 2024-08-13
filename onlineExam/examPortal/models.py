from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    text = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=1)  # A, B, C, or D

    def __str__(self):
        return self.text

class Exam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()
    is_completed = models.BooleanField(default=False)

    def mark_as_completed(self):
        self.is_completed = True
        self.completion_time = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.subject.name} exam by {self.user.username}'

class Answer(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=1)  # A, B, C, or D

    def __str__(self):
        return f'{self.exam.user.username} - {self.question.text}'


class UserRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    name = models.CharField(max_length=45)
    class1 = models.CharField(max_length=20)
    mobNo = models.CharField(max_length=13)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username# Or any other attribute like `self.email`
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Subject, Question, Exam, Answer
from django.utils import timezone
from datetime import timedelta

class ExamResultTestCase(TestCase):
    def setUp(self):
        # Set up data for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.subject = Subject.objects.create(name='Math')
        self.question1 = Question.objects.create(
            subject=self.subject, text='What is 2+2?',
            option1='3', option2='4', option3='5', option4='6',
            correct_option='B'
        )
        self.exam = Exam.objects.create(
            user=self.user, subject=self.subject,
            start_time=timezone.now(),
            end_time=timezone.now() + timedelta(minutes=30)
        )
        self.answer = Answer.objects.create(
            exam=self.exam, question=self.question1,
            selected_option='B'
        )

    def test_exam_result(self):
        # Calculate result
        questions = self.subject.question_set.all()
        answers = Answer.objects.filter(exam=self.exam)
        score = 0
        
        for question in questions:
            correct_option = question.correct_option
            selected_option = answers.filter(question=question).first().selected_option
            if selected_option == correct_option:
                score += 1
        
        self.assertEqual(score, 1)  # Assuming there is only one question and it's answered correctly

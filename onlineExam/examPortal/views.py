from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Subject, Question, Exam, Answer,UserRegistration
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control
from django.contrib.auth import logout



def welcome(request):
    if request.method == 'POST':
        logintype = request.POST.get('logintype')
        
        if logintype == 'signin':    
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            
            
            if user is not None:
                login(request, user)
                if user.is_staff:  # Check if the user is an admin
                    return redirect('/admin/')
                else:  # Otherwise, the user is a student
                    return redirect('selectSubj')
            else:
                error_message = 'Invalid username or password.'
                return render(request, 'examPortal/welcome.html', {'error_message': error_message})
        
        elif logintype == 'register':
            # for registration
            usernm = request.POST.get('usernm')
            name = request.POST.get('name')
            email = request.POST.get('email')
            mobNo = request.POST.get('mobNo')
            pass1 = request.POST.get('RegPassword')  
            class1 = request.POST.get('class1')
            age = request.POST.get('age')

            if User.objects.filter(username=usernm).exists():
                return render(request, 'examPortal/welcome.html', {
                    'error_message': 'Username already exists'
                })
            else:
                # Create the new user
                user = User.objects.create_user(username=usernm, password=pass1, email=email)  # Corrected to use pass1
                UserRegistration.objects.create(user=user, name=name, mobNo=mobNo,
                        class1=class1, age=age)
                login(request, user)
                return redirect('selectSubj')
        

         
    return render(request, 'examPortal/welcome.html')

#########################################################
###################  selectSubj  #############################
#########################################################

@login_required
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def selectSubj(request):
    subjects = Subject.objects.all()
    examType = request.POST.get('examType')
    logout1 = request.POST.get('logout')
    if logout1:
        logout(request)
        render(request,'welcome')

    if request.method == 'POST':
        subject_id = request.POST.get('subject')
        
        if not subject_id:
            messages.error(request, 'Subject not selected.')
            return redirect('selectSubj')

        try:
            subject = Subject.objects.get(id=subject_id)
        except Subject.DoesNotExist:
            messages.error(request, 'Invalid subject selected.')
            return redirect('selectSubj')

        if examType == 'mocktest':
            exam = Exam.objects.create(
                user=request.user,
                subject=subject,
                end_time=timezone.now() + timedelta(minutes=30)  # 30-minute timer
            )
            
            return redirect('examPage', exam_id=exam.id)

        elif examType == 'test':
            # Handle the test case
            existing_exam = Exam.objects.filter(user=request.user, subject=subject).first()
            if existing_exam:
                if existing_exam.is_completed:
                    messages.error(request, 'Exam is already completed.')
                    return redirect('examPage', exam_id=existing_exam.id)
                
                # If exam is not completed, redirect to the exam page
                return redirect('examPage', exam_id=existing_exam.id)
            else:
                messages.error(request, 'No existing Exam is Alloted')
                return redirect('selectSubj')

        else:
            messages.error(request, 'Invalid exam type selected.')
            return redirect('selectSubj')

    return render(request, 'examPortal/selectSubj.html', {'subjects': subjects})

#########################################################
###################  examPage  #############################
########################################################

@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@login_required
def examPage(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    logout1 = request.POST.get('logout')
    if logout1:
        logout(request)
        render(request,'welcome')


    if exam.user != request.user :
        messages.success(request, 'Exam can\'t Start. Invalid User')
        return redirect('selectSubj')
        
    if timezone.now() > exam.end_time:
        exam.is_completed = True
        exam.save()
        return redirect('exam_completed', exam_id=exam.id)

    if request.method == 'POST':
        for question in Question.objects.filter(subject=exam.subject):
            selected_option = request.POST.get(f'question{question.id}')
            if selected_option:  # Make sure an option was selected
                Answer.objects.create(exam=exam,question=question,
                    selected_option=selected_option)
                
        exam.is_completed = True
        exam.save()
        return redirect('exam_completed', exam_id=exam.id)

    questions = Question.objects.filter(subject=exam.subject)
    return render(request, 'examPortal/examPage.html', {'exam': exam, 'questions': questions})

#########################################################
###################  exam_completed  #############################
########################################################

@login_required
def exam_completed(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    logout1 = request.POST.get('logout')
    if logout1:
        logout(request)
        render(request,'welcome')

        
    if exam.user != request.user:
        messages.success(request, 'can\'t Show Result. Invalid User')
        return redirect('selectSubj')

    answers = Answer.objects.filter(exam=exam)
    questions = Question.objects.filter(subject=exam.subject)

    questions_with_answers = []
    for question in questions:
        answer = answers.filter(question=question).first()
        questions_with_answers.append({
            'question': question,
            'answer': answer,
            'selected_option_text': get_option_text(question, answer.selected_option) if answer else None,
            'correct_option_text': get_option_text(question, question.correct_option)
        })

    score = 0
    total_questions = questions.count()

    for qwa in questions_with_answers:
        question = qwa['question']
        answer = qwa['answer']

        correct_option = question.correct_option.strip().upper()       
        if correct_option in ['1','a']:
            correct_option = 'A'
        elif correct_option in ['2', 'b']:
            correct_option = 'B'
        elif correct_option in ['3', 'c']:
            correct_option = 'C'
        elif correct_option in ['4', 'd']:
            correct_option = 'D'
        
        if answer:
            selected_option = answer.selected_option.strip().upper()
            if selected_option == correct_option:
                score += 1

    # Mark exam as completed
    if exam.is_completed==False:
        exam.mark_as_completed()
        completion_tim=exam.completion_time
    else:
        completion_tim=exam.start_time + timedelta(minutes=20)

    context = {
        'exam': exam,
        'questions_with_answers': questions_with_answers,
        'score': score,
        'total_questions': total_questions,
        'start_time': exam.start_time,
        'completion_time': completion_tim,
    }
    
    return render(request, 'examPortal/exam_completed.html', context)

def get_option_text(question, option_key):
    option_map = {
        '1': question.option1,
        '2': question.option2,
        '3': question.option3,
        '4': question.option4,
        'A': question.option1,
        'B': question.option2,
        'C': question.option3,
        'D': question.option4,
    }
    return option_map.get(option_key.upper(), 'Unknown Option')


# def debug_exam_results(request, exam_id):
         
    
#     except Exam.DoesNotExist:
#         return render(request, 'examPortal/debug_exam_results.html', {'error': 'Exam not found'})









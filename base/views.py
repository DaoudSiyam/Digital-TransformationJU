from django.shortcuts import render, redirect
from .models import User, ShanghaiRanking, WebometricsRanking , THERanking, QSRanking ,WorkerFeedback , StudentFeedback
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = 'login_form')
def index_page(request):
    user = User.objects.get(id = request.user.id)
    if request.method == 'POST':
        if user.role == "worker":
            q1 = request.POST.get('worker_question1')
            q2 = request.POST.get('worker-question2')
            q3 = request.POST.get('worker-question3')
            q4 = request.POST.get('worker-question4')
        
            feedback = WorkerFeedback.objects.create(
                user=request.user,
                q1=q1,
                q2=q2,
                q3=q3,
                q4=q4,            
            )
            feedback.save()

        elif user.role == "student":
            q1 = request.POST.get('student-question1')
            q2 = request.POST.get('student-question2')
            q3 = request.POST.get('student-question3')
            q4 = request.POST.get('student-question4')
            q5 = request.POST.get('student-question5')
            q6 = request.POST.get('student-question6')            

            feedback = StudentFeedback.objects.create(
                user=request.user,
                q1=q1,
                q2=q2,
                q3=q3,
                q4=q4,
                q5=q5,
                q6=q6,                           
            )
            feedback.save()
            user.submitted = True
            user.save()
        return redirect('home')
                      
    return render(request, 'base/index.html')



def login_form(request):
    if request.user.is_authenticated:
        return redirect( 'home' )
    
    if request.method == 'POST':
        username = request.POST.get( 'username' )
        password = request.POST.get( 'password' )

        try:
            user = User.objects.get( username = username )
            # this is what we write to check if user exists
        except:
            HttpResponse( "user does not exist" )
    
        user = authenticate( request, username = username, password = password )

        if user is not None:
            login( request, user )
            return redirect( 'choices' )

    context = {}
    return render(request, 'base/login_form.html', context)



def logout_user(request):
    logout(request)
    return redirect('login_form')



def choices_page(request):
    user = User.objects.get(id = request.user.id)

    context = {
        'user' : user,
    }
    return render(request, 'base/choices.html', context)



def query_system(request):

    context = {}
    return render( request,'base/query-system.html', context )



def system_choices(request):

    context = {}
    return render(request, 'base/system-choices.html', context)



def qs(request):

    context = {}
    return render(request, 'base/qs.html', context)



def the(request):

    context = {}
    return render(request, 'base/the.html', context)



def webometrics(request):

    context = {}
    return render(request, 'base/webometrics.html', context)



def shanghai(request):
    q1 = request.GET.get( 'system' ) if request.GET.get( 'system' ) != None else ''
    q2 = request.GET.get( 'year' ) if request.GET.get( 'year' ) != None else ''
    
    subject_query = Q( subject__icontains = q1 )
    year_query = Q( year__icontains = q2 ) 

    query = subject_query & year_query

    rankings = ShanghaiRanking.objects.filter(query)

    context = {
        'rankings' : rankings,
    }
    return render(request, 'base/shanghai.html', context)



def admin_panel(request):
    user = User.objects.get(id = request.user.id)
    if not user.role == 'admin':
        return redirect('choices')
    
    worker_feedback = WorkerFeedback.objects.all()
    student_feedback = StudentFeedback.objects.all()



    # WORKERS SECTION
    worker_q1_percentage = 0
    worker_q2_percentage = 0
    worker_q3_percentage = 0
    worker_q4_percentage = 0

    for feedback in worker_feedback:
        worker_q1_percentage += feedback.q1
        worker_q2_percentage += feedback.q2
        worker_q3_percentage += feedback.q3
        worker_q4_percentage += feedback.q4

    worker_q1_percentage = worker_q1_percentage / worker_feedback.count()
    worker_q2_percentage = worker_q2_percentage / worker_feedback.count()
    worker_q3_percentage = worker_q3_percentage / worker_feedback.count()
    worker_q4_percentage = worker_q4_percentage / worker_feedback.count()



    # STUDENTS SECTION
    student_q1_percentage = 0
    student_q2_percentage = 0
    student_q3_percentage = 0
    student_q4_percentage = 0
    student_q5_percentage = 0
    student_q6_percentage = 0

    for feedback in student_feedback:
        student_q1_percentage += feedback.q1
        student_q2_percentage += feedback.q2
        student_q3_percentage += feedback.q3
        student_q4_percentage += feedback.q4
        student_q5_percentage += feedback.q5
        student_q6_percentage += feedback.q6
    
    student_q1_percentage = student_q1_percentage/student_feedback.count()
    student_q2_percentage = student_q2_percentage/student_feedback.count()
    student_q3_percentage = student_q3_percentage/student_feedback.count()
    student_q4_percentage = student_q4_percentage/student_feedback.count()
    student_q5_percentage = student_q5_percentage/student_feedback.count()
    student_q6_percentage = student_q6_percentage/student_feedback.count()

    context = {
        'student_feedback' : student_feedback,
        'worker_feedback': worker_feedback,


        'worker_q1_percentage' : worker_q1_percentage,
        'worker_q2_percentage' : worker_q2_percentage,
        'worker_q3_percentage' : worker_q3_percentage,
        'worker_q4_percentage' : worker_q4_percentage,


        'student_q1_percentage' : student_q1_percentage,
        'student_q2_percentage' : student_q2_percentage,
        'student_q3_percentage' : student_q2_percentage,
        'student_q4_percentage' : student_q4_percentage,
        'student_q5_percentage' : student_q5_percentage,
        'student_q6_percentage' : student_q6_percentage,
    }
    return render(request,'base/admin-panel.html', context)
from django.shortcuts import render, redirect
from .models import User, Feedback
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = 'login_form')
def index_page(request):
    user = User.objects.get(id = request.user.id)
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        q3 = request.POST.get('q3')
        q4 = request.POST.get('q4')
        q5 = request.POST.get('q5')
        q6 = request.POST.get('q6')
        q7 = request.POST.get('q7')
        q8 = request.POST.get('q8')
        q9 = request.POST.get('q9')
        q10 = request.POST.get('q10')
        q11 = request.POST.get('q11')

        feedback = Feedback.objects.create(
            user=request.user,
            q1=q1,
            q2=q2,
            q3=q3,
            q4=q4,
            q5=q5,
            q6=q6,
            q7=q7,
            q8=q8,
            q9=q9,
            q10=q10,
            q11=q11,
        )
        feedback.save()
        # user.submitted = True
        # user.save()
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

    context = {}
    return render(request, 'base/choices.html', context)

def query_system(request):

    context = {}
    return render( request,'base/query-system.html', context )
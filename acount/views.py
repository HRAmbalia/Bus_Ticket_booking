from django.shortcuts import render

# Create your views here.
from .forms import registerForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .models import contactUs
# 

def index(request):
    context = {}
    return render(request, 'acount/index.html', context)

def registerUser(request):
    form = registerForm()
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginUser') # 'login' specified in urls.py as name
    else:
        form = registerForm()
    context = {'form':form}
    return render(request, 'acount/register.html', context)

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Fill fields')
    context = {}
    return render(request, 'acount/login.html', context)

# this function is redirected to 'bookTicket/homePage'
# def homePage(request):
#     context = {}
#     return render(request, 'acount/home.html', context)
    # return render(request, 'bookTicket/home.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index')

def contactUsPage(request):
    # return HttpResponse("Contact Us")
    if request.method == 'POST':
        Uname = request.POST['nm']
        email = request.POST['mail']
        subject = request.POST['sub']
        message = request.POST['msg']

        if len(Uname)<2 or len(email)<6 or len(message)<5:
            messages.error(request, 'Fill form Correctly')
        else:
            contactObj = contactUs(name=Uname, email=email, subject=subject, message=message)
            contactObj.save()
            messages.success(request, 'Form submitted successfully')
    context = {}
    return render(request, 'acount/contactUs.html', context)

def aboutProject(request):
    # return HttpResponse("About Project")
    context = {}
    return render(request, 'acount/aboutProj.html', context)
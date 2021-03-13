from django.shortcuts import render

# Create your views here.
from .forms import registerForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
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
                return redirect('homePage')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Fill fields')
    context = {}
    return render(request, 'acount/login.html', context)

def homePage(request):
    context = {}
    return render(request, 'acount/home.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index')

def contactUs(request):
    # return HttpResponse("Contact Us")
    context = {}
    return render(request, 'acount/contactUs.html', context)

def aboutProject(request):
    # return HttpResponse("About Project")
    context = {}
    return render(request, 'acount/aboutProj.html', context)
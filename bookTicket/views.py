from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect
from django.contrib.auth import update_session_auth_hash
#

# def homePage(request):
    # return HttpResponse("abcdefgh")
    # context = {}
    # return render(request, 'bookticket/home.html', context)

def search(request):
    if request.user.is_authenticated:
        return HttpResponse("search")
    # context = {}
    # return render(request, 'bookticket/home.html', context)

def booking(request):
    if request.user.is_authenticated:
        return HttpResponse("booking")
    # context = {}
    # return render(request, 'bookticket/home.html', context)

def chgpass(request):
    # return HttpResponse("change password")
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('/')
        else:
            form = PasswordChangeForm(user=request.user)
        context = {'form':form}
        return render(request, 'bookticket/changepass.html', context)
    else:
        return redirect('/login')
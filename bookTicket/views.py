from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect
from django.contrib.auth import update_session_auth_hash
from .models import busDetails
from .models import ticketDetail
from django.contrib import messages
from datetime import date
import reportlab
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
#

# def homePage(request):
    # return HttpResponse("abcdefgh")
    # context = {}
    # return render(request, 'bookticket/home.html', context)

def search(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            arr = request.POST['from']
            request.session['arrival'] = arr
            dest = request.POST['to']
            request.session['destination'] = dest
            date = request.POST['traveldt']
            request.session['travelDate'] = date
            # ticketDetailObj = ticketDetail()
        #     all_bus_details = busDetails.objects.all()
        #     all_bus_details = busDetails.objects.filter(arrival=arr).filter(destination=dest)
        #     print(all_bus_details)
        #     if all_bus_details:
        #         context = {'arrival': arr, 'destination': dest, 'all_bus_details': all_bus_details}
        return render(request, 'bookticket/search.html')
        #     else:
        #         messages.info(request,"not found")
        #         redirect ('/search')
        # else:
        #     context = {}
        #     return render(request, 'bookticket/search.html', context)
    else:
        return redirect('/login')

def bookBus(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if 'arrival' in request.session:
                arr = request.session.get('arrival')
                print(arr)
            else:
                arr = request.POST['from']
                print(arr)
                request.session['arrival'] = arr
            # request.session['arrival'] = arr
            if 'destination' in request.session:
                dest = request.session.get('destination')
                print(dest)
            else:
                dest = request.POST['to']
                print(dest)
                request.session['destination'] = dest
            # request.session['destination'] = dest
            if 'travelDate' in request.session:
                date = request.session.get('travelDate')
                print(date)
            else:
                date = request.POST['traveldt']
                print(date)
                request.session['travelDate'] = date
            # request.session['travelDate'] = date
            all_bus_details = busDetails.objects.all()
            all_bus_details = busDetails.objects.filter(arrival=arr).filter(destination=dest)
            user_name = request.user.username
            for bus in all_bus_details:
                bus_ID = bus.busID
                bus_fare = bus.rent
            if 'pnm' in request.POST:
                passanger_name = request.POST['pnm']
                passanger_age = request.POST['pAge']
                passanger_gender = request.POST['gender']
                passanger_seatNo = request.POST['sno']
                ticketDetailObj = ticketDetail(userName=user_name, busID=bus_ID, journeyDate=date, totalFare=bus_fare, seatNo=passanger_seatNo, passName=passanger_name, passAge=passanger_age, PassGender=passanger_gender)
                ticketDetailObj.save()
                all_ticket_details = ticketDetail.objects.all()
                all_ticket_details = ticketDetail.objects.filter(busID=bus_ID).filter(journeyDate=date).filter(userName=user_name)
                totalFare = 0
                for fare in all_ticket_details:
                    totalFare = totalFare + fare.totalFare
                if all_bus_details:
                    context = {'arrival': arr, 'destination': dest, 'bus_details': all_bus_details, 'ticDetails':all_ticket_details, 'totalFare':totalFare}
                    return render(request, 'bookticket/bookBus.html', context)
            if all_bus_details:
                context = {'arrival': arr, 'destination': dest, 'bus_details': all_bus_details}
                return render(request, 'bookticket/bookBus.html', context)
            else:
                messages.info(request,"not found")
                redirect ('/search')
        else:
            context = {}
            return render(request, 'bookticket/bookBus.html', context)
    else:
        return redirect('/login')  


def booking(request):
    if request.user.is_authenticated:
        user_name = request.user.username
        today = date.today()
        oldTickets = ticketDetail.objects.all()
        oldTickets = ticketDetail.objects.filter(userName=user_name).filter(journeyDate__lt=today)
        newTickets = ticketDetail.objects.all()
        newTickets = ticketDetail.objects.filter(userName=user_name).filter(journeyDate__gt=today)
        context = {'oldticket':oldTickets, 'newticket':newTickets}
        return render(request, 'bookticket/myBookings.html', context)
    else:
        return redirect('/login')

def chgpass(request):
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


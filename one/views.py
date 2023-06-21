from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from.models import Flight,Passenger

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .forms import SingupUser

# Create your views here.
@login_required(login_url='login')
def index(request):
    flight = Flight.objects.all()
    return render(request,'one/index.html',{'flight':flight})


@login_required(login_url='login')
def flight(request,id):
    flight = Flight.objects.get(pk=id)
    passenger= flight.passengers.all()
    non_passenger = Passenger.objects.exclude(flights = flight).all()
    return render(request,'one/flight.html',
                  {'flight':flight,
                    'passenger':passenger,
                    'non_passenger':non_passenger,
                   
                   })
@login_required(login_url='login')
def book(request,flight_id):
    if request.method =="POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger_id = int(request.POST['passenger'])
        passenger = Passenger.objects.get(pk=passenger_id)
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse('flight',args=(flight.id,)))
    

#USER 

def login_view(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return render(request,'one/login.html',{'message':'invaild User'})
    return render(request,'one/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def user_signup(request):
    user = SingupUser()
    if request.method == 'POST':
        user = SingupUser(request.POST,request.FILES)
        if user.is_valid():
            user.save()
            return redirect('login')
        else:
            return render(request,'one/usersingup.html',{'user':user})

    return render(request,'one/usersingup.html',{'user':user})
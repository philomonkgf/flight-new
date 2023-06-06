from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from.models import Flight,Passenger

# Create your views here.

def index(request):
    flight = Flight.objects.all()
    return render(request,'one/index.html',{'flight':flight})

def flight(request,id):
    flight = Flight.objects.get(pk=id)
    passenger= flight.passengers.all()
    non_passenger = Passenger.objects.exclude(flights = flight).all()
    return render(request,'one/flight.html',
                  {'flight':flight,
                    'passenger':passenger,
                    'non_passenger':non_passenger,
                   
                   })

def book(request,flight_id):
    if request.method =="POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger_id = int(request.POST['passenger'])
        passenger = Passenger.objects.get(pk=passenger_id)
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse('flight',args=(flight.id,)))
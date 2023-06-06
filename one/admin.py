from django.contrib import admin
from .models import NewUser,Airport,Flight,Passenger

# Register your models here.

class NewFlight(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")



admin.site.register(NewUser)

admin.site.register(Airport)
admin.site.register(Flight,NewFlight)




admin.site.register(Passenger)
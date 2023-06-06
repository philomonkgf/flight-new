from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name='index'),
    path('flight_id/<int:id>',views.flight,name='flight'),
    path('book/<int:flight_id>',views.book,name='book')
]
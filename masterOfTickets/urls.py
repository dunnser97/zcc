from django.urls import path

from masterOfTickets import views

urlpatterns = [
# ex: /
    path('', views.home, name='home'),
    path('home', views.home, name='home')
]
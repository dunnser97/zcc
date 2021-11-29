from django.urls import path

from masterOfTickets import views

urlpatterns = [
# ex: /
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('showMeLists', views.showMeLists, name='showMeLists'),
    path('individual_ticket/<str:submitter>', views.individual_ticket, name='individual_ticket'),

]
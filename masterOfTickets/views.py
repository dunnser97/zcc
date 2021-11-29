from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from masterOfTickets import logins
import json

def home(request):
    return render(request, 'home.html')

def showMeLists(request):
    """
    Calls zendesk ticketing system and returns json object containing all tickets for account
    """
    response = requests.get("https://zccrivia.zendesk.com/api/v2/tickets.json",
                            auth=(logins.zcc["username"], logins.zcc["password"]))
    tickets = response.content
    tickets = json.loads(tickets)
    return JsonResponse(tickets)

def showMeIds(request, ticket_id):
    """
    Calls a particular ticket and displays details within
    """
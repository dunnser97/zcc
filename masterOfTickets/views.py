from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from masterOfTickets import logins
import json

def home(request):
    response = requests.get("https://zccrivia.zendesk.com/api/v2/tickets.json",
                            auth=(logins.zcc["username"], logins.zcc["password"]))
    if response.status_code != 200:
        HttpResponse("It appears the API is unavailable or something has gone horribly wrong...")
    else:
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
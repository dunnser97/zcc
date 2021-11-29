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
    response = requests.get("https://zccrivia.zendesk.com/api/v2/imports/tickets.json",
                            auth=(logins.zcc["username"], logins.zcc["password"]))
    if response.status_code==200:
        tickets = response.content
        tickets = json.loads(tickets)
        tickets = tickets["tickets"]
        return JsonResponse(tickets)
    else:
        HttpResponse("Looks like Something has gone horribly wrong... Please try again later!")

def showMeIds(request, ticket_id):
    """
    Calls a particular ticket and displays details within
    """
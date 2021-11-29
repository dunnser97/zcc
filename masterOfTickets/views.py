from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from masterOfTickets import logins
import json

def home(request):
    response = requests.get("https://zccrivia.zendesk.com/api/v2/tickets.json",
                            auth=(logins.zcc["username"], logins.zcc["password"]))
    if response.status_code != 200:
        return HttpResponse("It appears the API is unavailable or something has gone horribly wrong...")
    else:
        return render(request, 'home.html')

def individual_ticket(request, submitter):
    response_indiv = requests.get("https://zccrivia.zendesk.com/api/v2/tickets/" + submitter + ".json",
                                  auth=(logins.zcc["username"], logins.zcc["password"]))
    tickets = response_indiv.content
    tickets = json.loads(tickets)
    print(len(tickets))
    if ( len(tickets)==2 or response_indiv.status_code != 200) :
        return HttpResponse("Hmmm looks like the ticket you are looking for doesn't exist")
    else:
        return render(request, 'individual_ticket.html', {"result": tickets})

def showMeLists(request):
    """
    Calls zendesk ticketing system and returns json object containing all tickets for account
    """
    response = requests.get("https://zccrivia.zendesk.com/api/v2/tickets.json",
                            auth=(logins.zcc["username"], logins.zcc["password"]))
    tickets = response.content
    tickets = json.loads(tickets)
    return JsonResponse(tickets)

import requests
import logins
import json

def showMeLists(request):
    response = requests.get("https://zccrivia.zendesk.com/api/v2/imports/tickets.json",
                            auth=(logins.zcc["username"], logins.zcc["password"]))
    tickets = response.content
    tickets = json.loads(tickets)
    tickets = tickets["tickets"]
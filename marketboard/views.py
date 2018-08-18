from django.shortcuts import render

from marketboard.models import SERVER_LIST


def landing(request):
    return render(request, 'landing.html', {'server_list': [server[0] for server in SERVER_LIST]})


def home(request, server_name):
    pass

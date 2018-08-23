from datetime import timedelta

from django.shortcuts import render
from django.utils import timezone

from marketboard.models import SERVER_LIST, Transaction


def landing(request):
    return render(request, 'landing.html',
                  {'server_list': [server for server in SERVER_LIST]})


def home(request, server_name):
    recent_transactions = Transaction.objects.filter(
        server=server_name,
        transaction_time__gte=timezone.now() - timedelta(days=30))
    return render(request, 'home.html',
                  {'recent_transactions': recent_transactions,
                   'server': server_name})

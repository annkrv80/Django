from django.shortcuts import render
import logging
from datetime import datetime




logger = logging.getLogger(__name__)

def index(request):
    context = {'name': 'Anna'}
    return render(request, 'sem_3_1_app/main.html', context)

def about(request):
    context = {'datetime':datetime.now(), 'client_ip': '127.0.0.1'}
    return render (request, 'sem_3_1_app/about.html', context)

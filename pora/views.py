from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import *
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Paginator
from django.db.models import  Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

def raiz (request):
    return redirect('/inicio')

def login(request):
    return render(request, 'login.html')

def vendedores(request):
    vendedores = Vendedor.objects.all().order_by('-published_date')
    contexto = {'vendedores': vendedores}
    return render(request, 'responsive-tables.html',contexto)

def ticket(request):
    codigos = Codigo.objects.get(id=3)
    context = {'codigos':codigos,}

    return render(request, 'ticket.html', context)


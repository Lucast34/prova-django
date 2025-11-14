from django.shortcuts import render
from palavras.models import Palavras, Categoria, Regras


# Create your views here.

def index(request):
      return render(request,'palavras/index.html')
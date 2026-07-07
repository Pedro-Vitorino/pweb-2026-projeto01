from django.shortcuts import render
from .models import Ator, Sobre, Criador, Sinopse

def index(request):

    sinopse = Sinopse.objects.all()
    context= {
        "sinopse":sinopse,
    }
    return render(request, 'office/index.html', context)

def elenco(request):

    atores = Ator.objects.all()

    criadores = Criador.objects.all()
    
    context = {
        "atores": atores,

        "criadores": criadores,
    }
    return render(request, 'office/elenco.html', context)

def sobre(request):
    sobre_list = Sobre.objects.all()
    context= {
        "sobre": sobre_list,
    }

    return render(request, 'office/sobre.html', context)
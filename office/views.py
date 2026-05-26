from django.shortcuts import render

def index(request):

    sinopse = [
        {"data": "25 de Março de 2005", "sinopse": "The Office é uma série em formato de mockumentary (falso documentário) que retrata o cotidiano caótico e hilário dos funcionários de uma filial da empresa de papel Dunder Mifflin, em Scranton, Pensilvânia. O gerente regional, Michael Scott, é um chefe sem noção e egocêntrico que tenta liderar sua equipe lidando com diversas crises burocráticas."},

    ]

    context= {
        "sinopse":sinopse,
    }
    return render(request, 'office/index.html', context)

def elenco(request):
    return render(request, 'office/elenco.html')

def sobre(request):
    sobre_list = [
        {"criador" : "Pedro Emanuel Vitorino Dias Monteiro", "idade" : 17, "curiosidade" : "Fala inglês fluentemente"},
        {"criador" : "Nicolly Silva Gomes de Lima", "idade" : 16, "curiosidade" : "Tem um cachorrinho chamado Lucca"},
    ]

    context= {
        "sobre": sobre_list,
    }
    
    return render(request, 'office/sobre.html', context)
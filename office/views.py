from django.shortcuts import render

def index(request):
    return render(request, 'office/index.html')

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
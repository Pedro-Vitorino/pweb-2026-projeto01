from django.shortcuts import render

def index(request):
    return render(request, 'office/index.html')

def elenco(request):
    return render(request, 'office/elenco.html')

def sobre(request):
    return render(request, 'office/sobre.html')
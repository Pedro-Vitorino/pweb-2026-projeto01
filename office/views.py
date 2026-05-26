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

    atores = [
        {"Foto": "office/img/elenco/jim.jpg", "nome": "John Krasinski", "idade": 32, "categoria": "Ação/Comédia", "nasc": "Boston, MA", "Resumo": "John Krasinski é ator, diretor e roteirista. Ficou conhecido mundialmente por interpretar Jim Halpert em The Office. Além da comédia, também ganhou destaque no cinema ao dirigir e atuar em A Quiet Place, e protagonizou a série Tom Clancy's Jack Ryan."},
        {"Foto": "office/img/elenco/michael.jpg", "nome": "Steve Carrell", "idade": 65, "categoria": "Comédia", "nasc": "Concord, MA", "Resumo": "Steve Carell é ator, comediante e produtor. Tornou-se um dos nomes mais conhecidos da comédia ao interpretar Michael Scott em The Office. No cinema participou de filmes como The 40-Year-Old Virgin, Little Miss Sunshine e também deu voz ao Gru em Despicable Me."},
        {"Foto": "office/img/elenco/dwight.jpg", "nome": "Rainn Wilson", "idade": 40, "categoria": "Comédia", "nasc": "Seattle, WS", "Resumo": "Rainn Wilson ficou conhecido por interpretar Dwight Schrute em The Office, papel que marcou sua carreira. Além da atuação, também trabalhou como produtor e escritor e participou de diferentes séries e filmes de comédia ao longo dos anos."},
        {"Foto": "office/img/elenco/pam.jpg", "nome": "Jenna Fischer", "idade": 42, "categoria": "Romance/Comédia", "nasc": "Fort Wayne, IN", "Resumo": "Jenna Fischer ganhou reconhecimento ao interpretar Pam Beesly em The Office. Depois da série, participou de produções de televisão e cinema, especialmente no gênero de comédia, e também publicou livros contando parte de sua trajetória profissional."},
        {"Foto": "office/img/elenco/angela.jpg", "nome": "Angela Kinsey", "idade": 42, "categoria": "Romance/Comédia", "nasc": "Laffayete, LO", "Resumo": "Angela Kinsey ficou famosa por interpretar Angela Martin em The Office. Após o sucesso da série, continuou atuando em comédias e projetos para televisão, além de participar de podcasts e conteúdos sobre bastidores do entretenimento."},
        {"Foto": "office/img/elenco/ryan.jpg", "nome": "BJ Novak", "idade": 50, "categoria": "Romance/Comédia", "nasc": "Newton, MA", "Resumo": "B. J. Novak atuou como Ryan Howard em The Office e também foi um dos roteiristas e produtores da série. No cinema participou de filmes como Inglourious Basterds e também desenvolveu projetos próprios como diretor e escritor."},
    ]

    criadores = [
        {"Foto": "office/img/elenco/greg.jpg", "nome": "Greg Daniels", "idade": 62, "categoria": "Showrunner", "nasc": "Brooklyn, NY", "resumo" : "Greg Daniels é roteirista, produtor e showrunner. Ficou conhecido por adaptar a versão americana de The Office e também trabalhou em séries de sucesso como Parks and Recreation, The Simpsons e King of the Hill."},
        {"Foto": "office/img/elenco/mindy.jpg", "nome": "Mindy Kaling", "idade": 42, "categoria": "Roteirista", "nasc": "Cambridge, MA", "resumo" : "Mindy Kaling é atriz, roteirista e produtora. Ganhou destaque em The Office, onde interpretou Kelly Kapoor e trabalhou como roteirista. Depois criou e estrelou séries como The Mindy Project e participou de produções de comédia e cinema."},
         {"Foto": "office/img/elenco/ryan.jpg", "nome": "BJ Novak", "idade": 50, "categoria": "Ator/Roteirista", "nasc": "Newton, MA", "resumo" : "B. J. Novak atuou como Ryan Howard em The Office e também foi um dos roteiristas e produtores da série. Além da televisão, participou de filmes como Inglourious Basterds e trabalhou em projetos como escritor e diretor."},
        {"Foto": "office/img/elenco/mose.jpg", "nome": "Michael Schur", "idade": 35, "categoria": "Ator/Roteiro", "nasc": "Ann Arbor, MC", "resumo" : "Michael Schur é roteirista, produtor e ator. Em The Office, trabalhou como produtor e também interpretou Mose Schrute. Criou séries de sucesso como Brooklyn Nine-Nine, The Good Place e Parks and Recreation."},
        {"Foto": "office/img/elenco/toby.jpg", "nome": "Paul Libersteen", "idade": 700, "categoria": "NUNCA FEZ NADA QUE PRESTE", "nasc": "Area 51", "resumo" : "toby."},
    ]

    context = {
        "atores": atores,

        "criadores": criadores,
    }
    return render(request, 'office/elenco.html', context)

def sobre(request):
    sobre_list = [
        {"criador" : "Pedro Emanuel Vitorino Dias Monteiro", "idade" : 17, "curiosidade" : "Fala inglês fluentemente",  "foto": "office/img/pedro.png" },
        {"criador" : "Nicolly Silva Gomes de Lima", "idade" : 16, "curiosidade" : "Tem um cachorrinho chamado Lucca", "foto": "office/img/nicolly.png"},
    ]

    context= {
        "sobre": sobre_list,
    }

    return render(request, 'office/sobre.html', context)
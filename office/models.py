from django.db import models

class Sinopse(models.Model):
    data= models.DateField()
    sinopse = models.TextField()

    

    def __str__(self):
        return self.sinopse
    

class Atores(models.Model):
    nome = models.CharField(max_length=200)
    categoria = models.CharField(max_length=300)
    foto = models.ImageField(upload_to="atores/")
    nasc = models.CharField(max_length=300)
    resumo = models.TextField()
    idade = models.IntegerField()

    def __str__(self):
        return self.nome
    


class Criadores(models.Model):
    nome = models.CharField(max_length=200)
    categoria = models.CharField(max_length=300)
    foto = models.ImageField(upload_to="criadores/")
    nasc = models.CharField(max_length=300)
    resumo = models.TextField()
    idade = models.IntegerField()

    def __str__(self):
        return self.nome
    
class Sobre(models.Model):
    nome = models.CharField(max_length=200)
    foto = models.ImageField(upload_to="devs/")
    curiosidade = models.TextField()
    idade = models.IntegerField()

    def __str__(self):
        return self.nome
    
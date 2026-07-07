from django.db import models

class Sinopse(models.Model):
    data= models.DateField()
    sinopse = models.TextField()

    

    def __str__(self):
        return self.sinopse
    

class Ator(models.Model):
    nome = models.CharField(max_length=200)
    categoria = models.CharField(max_length=300)
    foto = models.ImageField(upload_to="atores/")
    nasc = models.CharField(max_length=300)
    resumo = models.TextField()
    idade = models.IntegerField()

    class Meta:
        verbose_name_plural= 'Atores'
    def __str__(self):
        return self.nome
    


class Criador(models.Model):
    nome = models.CharField(max_length=200)
    categoria = models.CharField(max_length=300)
    foto = models.ImageField(upload_to="criadores/")
    nasc = models.CharField(max_length=300)
    resumo = models.TextField()
    idade = models.IntegerField()

    class Meta:
        verbose_name_plural= 'Criadores'
    def __str__(self):
        return self.nome
    
class Sobre(models.Model):
    nome = models.CharField(max_length=200)
    foto = models.ImageField(upload_to="devs/")
    curiosidade = models.TextField()
    idade = models.IntegerField()

    class Meta:
        verbose_name_plural= 'Sobre'

    def __str__(self):
        return self.nome
    
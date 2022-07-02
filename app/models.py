from django.db import models
from datetime import datetime

class Produto(models.Model):
    
    ESCOLHAS = (
        ('1', 'Lanches Salgados'),
        ('2', 'Pizzas'),
        ('3', 'Bebidas'),
        ('4', 'Sobremesas'),
    )
    
    nome_produto = models.CharField(max_length=100)
    ingredientes = models.TextField()
    valor = models.CharField(max_length=10)
    imagem = models.ImageField(upload_to='./')
    categoria = models.CharField(max_length=1, choices=ESCOLHAS)
    data_produto = models.DateTimeField(default=datetime.now, blank=True)  
    visivel = models.BooleanField(default=True)
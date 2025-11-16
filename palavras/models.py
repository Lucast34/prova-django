from django.db import models

# Create your models here.

class Categoria(models.Model):
    tipo_execoes = models.CharField(max_length=88, null=False,blank= False)
    
    def __str__(self) -> str:
        return "Categoria [categoria = [{}]]".format(self.tipo_execoes)

class Regras(models.Model):
    
    tipo_uso = models.CharField(max_length=88, null=False,blank= False)
    
    tipo_escrita = models.CharField(max_length=88, null=False,blank= False)
    
    tipo_paronimos = models.CharField(max_length=88, null=False,blank= False)
    
    tipo_homonimos = models.CharField(max_length=88, null=False,blank= False)
    
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name = "palavras_categoria", null = False)
    
    def __str__(self):
        return "Palavra [palavra = [{}]]".format(self.palavras)

class Palavras(models.Model):
    palavras = models.CharField(max_length=88, null=False, blank= False)
    
    regra = models.ForeignKey(Regras, on_delete=models.CASCADE, related_name = "palavra_regras", null = False)
    

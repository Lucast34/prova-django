from django.db import models

# Create your models here.

class palavras(models.Model):
    palavras = models.CharField(max_length=88, null=False, blank= False)
    
    def __str__(self):
        return "Palavra [palavra = [{}]]".format(self.palavras)
    

class categoria(models.Model):
    tipo_execoes = models.models.CharField(max_length=88, null=False,blank= False)
    
    def __str__(self) -> str:
        return "Categoria [categoria = [{}]]".format(self.tipo_execoes)

class regras(models.Model):
    
    tipo_uso = models.models.CharField(max_length=88, null=False,blank= False)
    
    tipo_escrita = models.models.CharField(max_length=88, null=False,blank= False)
    
    tipo_paronimos = models.models.CharField(max_length=88, null=False,blank= False)
    
    tipo_homonimos = models.models.CharField(max_length=88, null=False,blank= False)
    
    fk_tb_categoria_id = models.models.ForeignKey(categoria, on_delete=models.CASCADE, related_name = "palavras_categoria", null = False)
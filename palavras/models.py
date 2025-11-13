from django.db import models

# Create your models here.

class palavras(models.Model):
    palavras = models.CharField(max_length=88, null=False, blank= False)
    
    def __str__(self):
        return "Palavra [palavra = [{}]]".format(self.palavras)
    
    
class regras(models.Model):
    tipo_uso = models.models.CharField(max_length=88, null=False,blank= False)
    pass
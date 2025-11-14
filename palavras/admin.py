from django.contrib import admin

import palavras.models as pl

# Register your models here.

admin.site.register(pl.Palavras)
admin.site.register(pl.Categoria)
admin.site.register(pl.Regras)
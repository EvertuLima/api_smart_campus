from django.contrib import admin
from .models import Material, Espaco, Servidores

# Register your models here.

@admin.register(Espaco)
class EspacoAdmin(admin.ModelAdmin):
    ...

@admin.register(Servidores)
class ServidoresAdmin(admin.ModelAdmin):
    ...

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    ...
    

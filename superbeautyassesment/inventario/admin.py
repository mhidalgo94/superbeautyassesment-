from django.contrib import admin

from .models import EquipoModel
from .models import EquipoUsuarioModel
# Register your models here.

class Equipo(admin.ModelAdmin):
    list_display = ('id','referencia','marca','tipo')
    list_filter = ('tipo',)
    search_fields = ('referencia',)

class EquipoUsuario(admin.ModelAdmin):
    list_display = ('id','equipo','usuario','fecha_asignacion')
    list_filter = ('usuario','fecha_asignacion',)
    # search_fields = ('usuario','fecha_entrega)


admin.site.register(EquipoModel, Equipo)
admin.site.register(EquipoUsuarioModel, EquipoUsuario)
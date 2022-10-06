from django.contrib import admin

from .models import EquipoModel,EquipoUsuarioModel
# Register your models here.
admin.site.site_header = 'Control Inventario Superbeauty'

class EquipoAdminView(admin.ModelAdmin):
    list_display = ('id','referencia','marca','tipo')
    list_filter = ('tipo',)
    search_fields = ('referencia',)

class EquipoUsuarioAdminView(admin.ModelAdmin):
    list_display = ('id','equipo','usuario','fecha_asignacion')
    list_filter = ('usuario','fecha_asignacion',)
    # readonly_fields = ("equipo",)
    # search_fields = ('usuario','fecha_entrega)
    

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        '''
            Esta funcion se sobre escribio para no mostrar equipos previamente asignados..
            Enlace Documentacion:
            https://docs.djangoproject.com/en/4.1/ref/contrib/admin/
            https://books.agiliq.com/projects/django-admin-cookbook/en/latest/filter_fk_dropdown.html
        '''
        if db_field.name == "equipo":
            kwargs["queryset"] = EquipoModel.objects.filter(equip__isnull=True) # Filtro para excluir equipos no asignados con related_name 'equip'
        return super().formfield_for_foreignkey(db_field, request, **kwargs)




admin.site.register(EquipoModel, EquipoAdminView)
admin.site.register(EquipoUsuarioModel, EquipoUsuarioAdminView)
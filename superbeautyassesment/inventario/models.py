from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class EquipoModel(models.Model):
    referencia = models.CharField(verbose_name=_("Referencia"), max_length=50)
    marca = models.CharField(verbose_name=_("Marca"),max_length=50)
    procesador = models.CharField(verbose_name=_('Procesador'), max_length=50)
    memoria = models.CharField(verbose_name=_('Memoria'), max_length=50)
    disco = models.CharField(verbose_name=_('Disco'), max_length=50)
    tipo = models.CharField(verbose_name=_('Tipo'), max_length=50)

    def __str__(self):
        return f"{self.referencia}"

    class Meta:
        verbose_name = _('Equipo')
        verbose_name_plural  = _('Equipos')


class EquipoUsuarioModel(models.Model):
    equipo =  models.ForeignKey(EquipoModel, verbose_name=_("Equipo"),on_delete=models.CASCADE,related_name="equip",blank=True, null=True,)
    usuario = models.ForeignKey(User,verbose_name=_("Usuario"), on_delete=models.CASCADE)
    fecha_asignacion = models.DateField(verbose_name=_("Fecha de Asignación"))
    fecha_entrega = models.DateField(verbose_name=_("Fecha de Entrega"))


    def __str__(self):
        return f"{self.usuario}"

    class Meta:
        verbose_name = _("Equipo Usuario")
        verbose_name_plural = _("Equipos Usuarios")




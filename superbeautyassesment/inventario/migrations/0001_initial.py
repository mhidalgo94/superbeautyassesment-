# Generated by Django 3.2 on 2022-10-06 00:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia', models.CharField(max_length=50, verbose_name='Referencia')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
                ('procesador', models.CharField(max_length=50, verbose_name='Procesador')),
                ('memoria', models.CharField(max_length=50, verbose_name='Memoria')),
                ('disco', models.CharField(max_length=50, verbose_name='Disco')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
            },
        ),
        migrations.CreateModel(
            name='EquipoUsuarioModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_asignacion', models.DateField(verbose_name='Fecha de Asignación')),
                ('fecha_entrega', models.DateField(verbose_name='Fecha de Entrega')),
                ('equipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='equip', to='inventario.equipomodel', verbose_name='Equipo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Equipo Usuario',
                'verbose_name_plural': 'Equipos Usuarios',
            },
        ),
    ]

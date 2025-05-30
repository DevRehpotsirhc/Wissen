# Generated by Django 5.2 on 2025-05-21 17:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('faltas', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='falta',
            name='id_administrador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.administrador'),
        ),
        migrations.AddField(
            model_name='falta',
            name='id_docente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.docente'),
        ),
        migrations.AddField(
            model_name='falta',
            name='id_estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuarios.estudiante'),
        ),
        migrations.AddField(
            model_name='falta',
            name='id_justificacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='faltas.justificacion'),
        ),
    ]

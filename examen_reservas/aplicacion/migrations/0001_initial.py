# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-18 17:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreC', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreD', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaDeReserva', models.DateTimeField(default=django.utils.timezone.now)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Cliente')),
                ('destino', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Destino')),
            ],
        ),
    ]

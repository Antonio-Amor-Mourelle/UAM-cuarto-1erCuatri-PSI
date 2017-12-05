# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20171118_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=50)),
                ('familyName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Orderline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit', models.IntegerField(default=0)),
                ('pricePerUnit', models.DecimalField(max_digits=5, decimal_places=2)),
                ('order', models.ForeignKey(related_name='orderLines', to='placeorder.Order')),
                ('product', models.ForeignKey(related_name='productLines', to='shop.Product')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('catName', models.CharField(unique=True, max_length=128)),
                ('catSlug', models.SlugField(unique=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prodName', models.CharField(unique=True, max_length=128)),
                ('prodSlug', models.SlugField(unique=True, max_length=128)),
                ('image', models.ImageField(upload_to='images/products')),
                ('description', models.CharField(max_length=1024)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('stock', models.IntegerField(default=0)),
                ('availability', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(to='onlineshop.Category')),
            ],
        ),
    ]

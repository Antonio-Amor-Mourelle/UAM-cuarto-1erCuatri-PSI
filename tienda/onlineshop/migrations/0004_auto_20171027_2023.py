# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0003_auto_20171027_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='catSlug',
            field=models.SlugField(unique=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='product',
            name='prodSlug',
            field=models.SlugField(unique=True, max_length=128),
        ),
    ]

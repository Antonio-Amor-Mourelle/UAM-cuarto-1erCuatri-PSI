# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0002_auto_20171027_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='catSlug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='prodSlug',
            field=models.SlugField(),
        ),
    ]

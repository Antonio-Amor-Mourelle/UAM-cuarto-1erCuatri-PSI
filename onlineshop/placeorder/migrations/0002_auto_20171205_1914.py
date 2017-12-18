# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placeorder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderline',
            old_name='unit',
            new_name='units',
        ),
        migrations.AlterField(
            model_name='order',
            name='zip',
            field=models.CharField(max_length=20),
        ),
    ]

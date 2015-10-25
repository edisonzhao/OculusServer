# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oculus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='x',
            field=models.DecimalField(max_digits=30, decimal_places=15),
        ),
        migrations.AlterField(
            model_name='position',
            name='y',
            field=models.DecimalField(max_digits=30, decimal_places=15),
        ),
        migrations.AlterField(
            model_name='position',
            name='z',
            field=models.DecimalField(max_digits=30, decimal_places=15),
        ),
    ]

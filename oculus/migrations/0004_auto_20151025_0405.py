# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oculus', '0003_position_w'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='w',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='x',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='y',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='z',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]

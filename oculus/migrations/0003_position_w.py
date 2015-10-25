# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oculus', '0002_auto_20151025_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='w',
            field=models.DecimalField(default=1, max_digits=30, decimal_places=15),
        ),
    ]

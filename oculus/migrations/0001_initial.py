# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.DecimalField(max_digits=15, decimal_places=15)),
                ('y', models.DecimalField(max_digits=15, decimal_places=15)),
                ('z', models.DecimalField(max_digits=15, decimal_places=15)),
                ('time_received', models.DateField()),
            ],
        ),
    ]

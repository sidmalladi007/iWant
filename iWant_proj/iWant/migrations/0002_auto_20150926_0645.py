# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iWant', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wish',
            options={'ordering': ('-created_date',)},
        ),
        migrations.AddField(
            model_name='wish',
            name='brand',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='wish',
            name='condition',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AlterField(
            model_name='wish',
            name='created_date',
            field=models.DateTimeField(),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iWant', '0002_auto_20150926_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='details',
            field=models.TextField(default=''),
        ),
    ]

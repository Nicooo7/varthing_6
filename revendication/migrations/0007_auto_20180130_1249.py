# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-30 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revendication', '0006_auto_20180130_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='organisation_en_lien',
            field=models.ManyToManyField(null=True, to='revendication.Organisation'),
        ),
    ]

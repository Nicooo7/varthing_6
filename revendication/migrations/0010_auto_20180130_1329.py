# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-30 12:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('revendication', '0009_auto_20180130_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='organisations_en_lien',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='revendication.Organisation'),
        ),
    ]
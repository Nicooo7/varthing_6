# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-02 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revendication', '0012_auto_20180202_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soutien',
            name='lien',
            field=models.CharField(choices=[('CR', 'createur'), ('SO', 'soutien')], max_length=2),
        ),
    ]

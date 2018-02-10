# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-02 13:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('revendication', '0011_auto_20180202_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisation',
            name='soutiens',
        ),
        migrations.AddField(
            model_name='soutien',
            name='organisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='revendication.Organisation'),
        ),
        migrations.AlterField(
            model_name='soutien',
            name='lien',
            field=models.CharField(choices=[('CR', 'createur'), ('SO', 'soutien'), ('GE', 'gestionnaire')], max_length=2),
        ),
    ]
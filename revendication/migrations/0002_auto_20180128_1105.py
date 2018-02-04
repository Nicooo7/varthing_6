# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-28 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revendication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='competence',
            field=models.ManyToManyField(blank=True, null=True, to='revendication.Competence'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='document',
            field=models.ManyToManyField(blank=True, null=True, to='revendication.Document'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='evenement',
            field=models.ManyToManyField(blank=True, null=True, to='revendication.Evenement'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='lieu_action',
            field=models.ManyToManyField(blank=True, to='revendication.Lieu'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='organisations_en_lien',
            field=models.ManyToManyField(blank=True, null=True, related_name='_organisation_organisations_en_lien_+', to='revendication.Organisation'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='petition',
            field=models.ManyToManyField(blank=True, null=True, to='revendication.Petition'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='proposition',
            field=models.ManyToManyField(blank=True, null=True, to='revendication.Proposition'),
        ),
    ]

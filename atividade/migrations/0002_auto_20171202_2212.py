# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-02 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atividade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='data_fim',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='data_inicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='prazo',
            field=models.DateField(blank=True, null=True),
        ),
    ]

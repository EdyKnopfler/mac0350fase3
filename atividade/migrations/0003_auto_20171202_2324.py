# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-02 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atividade', '0002_auto_20171202_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='data_fim',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='data_inicio',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='prazo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

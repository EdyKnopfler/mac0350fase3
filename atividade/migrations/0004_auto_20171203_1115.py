# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atividade', '0003_auto_20171202_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='data_fim',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='data_inicio',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='prazo',
            field=models.DateField(null=True),
        ),
    ]

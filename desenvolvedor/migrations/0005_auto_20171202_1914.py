# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-02 19:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('requisito', '0004_auto_20171202_1207'),
        ('desenvolvedor', '0004_auto_20171201_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('prazo', models.DateField()),
                ('dev_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requisitos', to='desenvolvedor.Desenvolvedor')),
                ('req_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='desenvolvedores', to='requisito.Requisito')),
            ],
        ),
        migrations.RemoveField(
            model_name='atividades',
            name='dev_id',
        ),
        migrations.RemoveField(
            model_name='atividades',
            name='req_id',
        ),
        migrations.DeleteModel(
            name='Atividades',
        ),
    ]
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class AnaliseDeRequisitos(models.Model):
    nome = models.CharField(max_length=255, null=False)
    descricao = models.TextField()

    class Meta:
        db_table = 'analise_de_requisitos'


class Equipe(models.Model):
    dev_id = models.ForeignKey('desenvolvedor.Desenvolvedor', on_delete=models.CASCADE, related_name='projetos')
    ar_id = models.ForeignKey(AnaliseDeRequisitos, on_delete=models.CASCADE, related_name='desenvolvedores')

    class Meta:
        db_table = 'equipe'

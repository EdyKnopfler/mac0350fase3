# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Atividade(models.Model):
    dev_id = models.ForeignKey('desenvolvedor.Desenvolvedor', on_delete=models.CASCADE, related_name='requisitos')
    req_id = models.ForeignKey('requisito.Requisito', on_delete=models.CASCADE, related_name='desenvolvedores')
    descricao = models.TextField()
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    prazo = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'atividade'

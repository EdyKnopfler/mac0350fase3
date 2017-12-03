# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Atividade(models.Model):
    dev_id = models.ForeignKey('desenvolvedor.Desenvolvedor', on_delete=models.CASCADE, related_name='requisitos')
    req_id = models.ForeignKey('requisito.Requisito', on_delete=models.CASCADE, related_name='desenvolvedores')
    descricao = models.TextField()
    data_inicio = models.CharField(max_length=255, null=True, blank=True)
    data_fim = models.CharField(max_length=255, null=True, blank=True)
    prazo = models.CharField(max_length=255, null=True, blank=True)


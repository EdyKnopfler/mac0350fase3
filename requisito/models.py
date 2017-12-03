# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Requisito(models.Model):
    CHOICES = (('funcional', 'Funcional'), ('dados', 'Dados'))
    tipo = models.CharField(max_length=255, null=False, choices=CHOICES, default=None)
    nome = models.CharField(max_length=255, null=False)
    detalhes = models.TextField(null=True, blank=True)
    ar_id = models.ForeignKey('analise_de_requisitos.AnaliseDeRequisitos', on_delete=models.CASCADE)

    class Meta:
        db_table = 'requisito'

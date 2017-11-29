# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Requisito(models.Model):
    nome = models.CharField(max_length=255, null=False)
    tipo = models.CharField(max_length=255, null=False)
    detalhes = models.TextField(null=False)
    ar_id = models.ForeignKey('analise_de_requisitos.AnaliseDeRequisitos', on_delete=models.CASCADE)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class AnaliseDeRequisitos(models.Model):
    nome = models.CharField(max_length=255, null=False)
    descricao = models.TextField(null=False)

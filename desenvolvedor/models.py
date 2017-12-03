# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Desenvolvedor(models.Model):
    nome = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False, unique=True)
    senha = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'desenvolvedor'

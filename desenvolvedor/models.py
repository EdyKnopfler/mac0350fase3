# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Desenvolvedor(models.Model):
    nome = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False, unique=True)
    senha = models.CharField(max_length=255, null=False)


class Equipe(models.Model):
    desenvolvedor = models.ForeignKey(Desenvolvedor, on_delete=models.CASCADE, related_name='projetos')
    analise_de_requisito = models.ForeignKey('analise_de_requisitos.AnaliseDeRequisitos', on_delete=models.CASCADE, related_name='desenvolvedores')


class Atividades(models.Model):
    desenvolvedor = models.ForeignKey(Desenvolvedor, on_delete=models.CASCADE, related_name='requisitos')
    requisito = models.ForeignKey('requisito.Requisito', on_delete=models.CASCADE, related_name='desenvolvedores')

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from desenvolvedor.models import Desenvolvedor
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def index(request):
    try:
        desenvolvedor = Desenvolvedor.objects.get(id=request.session['desenvolvedor_id'])
        projetos = desenvolvedor.projetos.all
        return render(request, 'analise_de_requisitos/index.html', {'desenvolvedor': desenvolvedor, 'projetos': projetos})
    except KeyError:
        messages.warning(request, 'Desenvolvedor não logado')
        return redirect('desenvolvedor_index')

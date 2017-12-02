# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from analise_de_requisitos.models import AnaliseDeRequisitos
from requisito.models import Requisito
from requisito.forms import RequisitoForm
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.

def new(request):
    form = RequisitoForm()
    return render(request, 'requisito/new.html', {'form': form})


def create(request):
    form = RequisitoForm(request.POST)
    if form.is_valid():
        projeto_atual = AnaliseDeRequisitos.objects.get(id=request.session['ar_id'])
        novo_requisito = Requisito(tipo=request.POST['tipo'], nome=request.POST['nome'],
                                   detalhes=request.POST['detalhes'], ar_id=projeto_atual)
        novo_requisito.save()
        messages.success(request, 'Requisito criado com sucesso')
    else:
        messages.warning(request, 'Formulário inválido')
    return redirect('ar_show', request.session['ar_id'])

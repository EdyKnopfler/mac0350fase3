# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from analise_de_requisitos.models import AnaliseDeRequisitos
from atividade.models import Atividade
from requisito.models import Requisito
from requisito.forms import RequisitoForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction


def show(request, requisito_id):
    request.session['requisito_id'] = requisito_id
    requisito = Requisito.objects.get(id=requisito_id)
    atividades = Atividade.objects.filter(req_id=requisito)
    return render(request, 'requisito/show.html', {'requisito': requisito, 'atividades': atividades})


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


def edit(request):
    antigo_requisito = Requisito.objects.get(id=request.session['requisito_id'])
    form = RequisitoForm(instance=antigo_requisito)
    return render(request, 'requisito/edit.html', {'form': form})


def update(request):
    antigo_requisito = Requisito.objects.get(id=request.session['requisito_id'])
    requisito_atualizado = RequisitoForm(request.POST, instance=antigo_requisito)
    if requisito_atualizado.is_valid():
        requisito_atualizado.save()
        messages.success(request, 'Requisito atualizado com sucesso')
    else:
        messages.warning(request, 'Falha na atualização do Requisito')
    return redirect('requisito_show', request.session['requisito_id'])


def delete(request):
    with transaction.atomic():
        Requisito.objects.get(id=request.session['requisito_id']).delete()
    del request.session['requisito_id']
    messages.success(request, 'Requisito apagado com sucesso')
    return redirect('ar_show', request.session['ar_id'])

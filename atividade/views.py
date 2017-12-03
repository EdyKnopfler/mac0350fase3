# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from desenvolvedor.models import Desenvolvedor
from requisito.models import Requisito
from atividade.models import Atividade
from atividade.forms import AtividadeForm
from django.shortcuts import render, redirect
from django.contrib import messages


def show(request, atividade_id):
    request.session['atividade_id'] = atividade_id
    atividade = Atividade.objects.get(id=atividade_id)
    return render(request, 'atividade/show.html', {'atividade': atividade})


def new(request):
    form = AtividadeForm()
    return render(request, 'atividade/new.html', {'form': form})


def create(request):
    form = AtividadeForm(request.POST)
    if form.is_valid():
        desenvolvedor_atual = Desenvolvedor.objects.get(id=request.session['desenvolvedor_id'])
        requisito_atual = Requisito.objects.get(id=request.session['requisito_id'])
        Atividade(dev_id=desenvolvedor_atual, req_id=requisito_atual, descricao=request.POST['descricao'],
                  data_inicio=request.POST['data_inicio'], data_fim=request.POST['data_fim'],
                  prazo=request.POST['prazo']).save()
        messages.success(request, 'Atividade criada com sucesso')
    else:
        messages.warning(request, 'Formulário inválido')
    return redirect('requisito_show', request.session['requisito_id'])


def edit(request):
    antiga_atividade = Atividade.objects.get(id=request.session['atividade_id'])
    form = AtividadeForm(instance=antiga_atividade)
    return render(request, 'atividade/edit.html', {'form': form})


def update(request):
    antiga_atividade = Atividade.objects.get(id=request.session['atividade_id'])
    atividade_atualizada = AtividadeForm(request.POST, instance=antiga_atividade)
    if atividade_atualizada.is_valid():
        atividade_atualizada.save()
        messages.success(request, 'Atividade atualizada com sucesso')
    else:
        messages.warning(request, 'Falha na atualização da Atividade')
    return redirect('atividade_show', request.session['atividade_id'])


def delete(request):
    Atividade.objects.get(id=request.session['atividade_id']).delete()
    del request.session['atividade_id']
    messages.success(request, 'Atividade apagada com sucesso')
    return redirect('requisito_show', request.session['requisito_id'])

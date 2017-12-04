# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from analise_de_requisitos.sql import *

from desenvolvedor.models import Desenvolvedor
from analise_de_requisitos.models import AnaliseDeRequisitos, Equipe
from atividade.models import Atividade
from requisito.models import Requisito
from .forms import AnaliseDeRequisitosForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction


def index(request):
    desenvolvedor_id = request.session['desenvolvedor_id']
    cursor_projetos = projetos_desenvolvedor(desenvolvedor_id)
    cursor_atividades = atividades_desenvolvedor(desenvolvedor_id)
    resposta = render(request, 'analise_de_requisitos/index.html',
                      {'todos_projetos': cursor_projetos, 
                       'todas_atividades': cursor_atividades})
    cursor_projetos.close()
    cursor_atividades.close()
    return resposta


def show(request, ar_id):
    request.session['ar_id'] = ar_id
    analise_de_requisito = AnaliseDeRequisitos.objects.get(id=ar_id)
    requisitos = Requisito.objects.filter(ar_id=analise_de_requisito)
    cursor_desenvolvedores = desenvolvedores_projeto(ar_id)
    resposta = render(request, 'analise_de_requisitos/show.html',
                      {'analise_de_requisito': analise_de_requisito, 'requisitos': requisitos,
                       'equipe': cursor_desenvolvedores})
    cursor_desenvolvedores.close()
    return resposta


def new(request):
    form = AnaliseDeRequisitosForm()
    return render(request, 'analise_de_requisitos/new.html', {'form': form})


def create(request):
    form = AnaliseDeRequisitosForm(request.POST)
    if form.is_valid():
        with transaction.atomic():
            novo_projeto = AnaliseDeRequisitos(nome=request.POST['nome'], descricao=request.POST['descricao'])
            novo_projeto.save()
            Equipe(dev_id_id=request.session['desenvolvedor_id'], ar_id_id=novo_projeto.id).save()
        messages.success(request, 'Projeto criado com sucesso')
    else:
        messages.warning(request, 'Falha na criação do Projeto')
    return redirect('ar_index')


def edit(request):
    antigo_projeto = AnaliseDeRequisitos.objects.get(id=request.session['ar_id'])
    form = AnaliseDeRequisitosForm(instance=antigo_projeto)
    return render(request, 'analise_de_requisitos/edit.html', {'form': form})


def update(request):
    antigo_projeto = AnaliseDeRequisitos.objects.get(id=request.session['ar_id'])
    projeto_atualizado = AnaliseDeRequisitosForm(request.POST, instance=antigo_projeto)
    if projeto_atualizado.is_valid():
        projeto_atualizado.save()
        messages.success(request, 'Projeto atualizado com sucesso')
        return redirect('ar_show', request.session['ar_id'])
    else:
        messages.warning(request, 'Falha na atualização do Projeto')
        return redirect('ar_edit')


def delete(request):
    with transaction.atomic():
        AnaliseDeRequisitos.objects.get(id=request.session['ar_id']).delete()
    del request.session['ar_id']
    messages.success(request, 'Projeto apagado com sucesso')
    return redirect('ar_index')


def remove_dev(request, dev_id):
    if possui_atividade(request, dev_id):
        messages.warning(request, 'O Desenvolvedor ainda possui atividades pendentes a este Projeto')
        return redirect('ar_show', request.session['ar_id'])
    Equipe.objects.get(dev_id=dev_id, ar_id=request.session['ar_id']).delete()
    messages.success(request, 'Desenvolvedor removido do Projeto com sucesso')
    if int(dev_id) == request.session['desenvolvedor_id']:
        del request.session['ar_id']
        return redirect('ar_index')
    else:
        return redirect('ar_show', request.session['ar_id'])


def select_dev(request):
    equipe_ids = Equipe.objects.values_list('dev_id_id').filter(ar_id_id=request.session['ar_id'])
    outros_desenvolvedores = Desenvolvedor.objects.exclude(id__in=equipe_ids)
    return render(request, 'analise_de_requisitos/select_dev.html', {'outros_desenvolvedores': outros_desenvolvedores})


def add_dev(request, dev_id):
    Equipe(dev_id_id=dev_id, ar_id_id=request.session['ar_id']).save()
    messages.success(request, 'Desenvolvedor adicionado ao Projeto com sucesso')
    return redirect('ar_show', request.session['ar_id'])


def possui_atividade(request, dev_id):
    atividades = Atividade.objects.filter(dev_id=dev_id)
    for atividade in atividades:
        if atividade.req_id.ar_id.id == int(request.session['ar_id']):
            return True
    return False


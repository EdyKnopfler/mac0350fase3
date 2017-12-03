# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from analise_de_requisitos.sql import sql

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
    sql.projetos_desenvolvedor(desenvolvedor_id)
    sql.atividades_desenvolvedor(desenvolvedor_id)
    resposta = render(request, 'analise_de_requisitos/index.html',
                      {'todos_projetos': sql.cursor_projetos, 
                       'todas_atividades': sql.cursor_atividades})
    return resposta


def show(request, ar_id):
    request.session['ar_id'] = ar_id
    analise_de_requisito = AnaliseDeRequisitos.objects.get(id=ar_id)
    requisitos = Requisito.objects.filter(ar_id=analise_de_requisito)
    #equipe = analise_de_requisito.desenvolvedores.all()
    sql.desenvolvedores_projeto(ar_id)
    return render(request, 'analise_de_requisitos/show.html',
                  {'analise_de_requisito': analise_de_requisito, 'requisitos': requisitos,
                   'equipe': sql.cursor_desenvolvedores})


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
    AnaliseDeRequisitos.objects.get(id=request.session['ar_id']).delete()
    del request.session['ar_id']
    messages.success(request, 'Projeto apagado com sucesso')
    return redirect('ar_index')


def remove_dev(request, dev_id):
    Equipe.objects.get(dev_id=dev_id, ar_id=request.session['ar_id']).delete()
    messages.success(request, 'Desenvolvedor removido do Projeto com sucesso')
    if int(dev_id) == request.session['desenvolvedor_id']:
        del request.session['ar_id']
        return redirect('ar_index')
    else:
        return redirect('ar_show', request.session['ar_id'])


def select_dev(request):
    projeto_atual = AnaliseDeRequisitos.objects.get(id=request.session['ar_id'])
    equipe = projeto_atual.desenvolvedores.all()
    equipe_ids = [desenvolvedor.dev_id.id for desenvolvedor in equipe]
    outros_desenvolvedores = Desenvolvedor.objects.exclude(id__in=equipe_ids)
    if outros_desenvolvedores.count() == 0:
        messages.warning(request, 'Não há desenvolvedores disponíveis')
    return render(request, 'analise_de_requisitos/select_dev.html', {'outros_desenvolvedores': outros_desenvolvedores})


def add_dev(request, dev_id):
    projeto_atual = AnaliseDeRequisitos.objects.get(id=request.session['ar_id'])
    novo_desenvolvedor = Desenvolvedor.objects.get(id=dev_id)
    Equipe(dev_id=novo_desenvolvedor, ar_id=projeto_atual).save()
    messages.success(request, 'Desenvolvedor adicionado ao Projeto com sucesso')
    return redirect('ar_show', request.session['ar_id'])

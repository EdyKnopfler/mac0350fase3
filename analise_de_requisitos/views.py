# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from desenvolvedor.models import Desenvolvedor, Equipe
from analise_de_requisitos.models import AnaliseDeRequisitos
from .forms import AnaliseDeRequisitosForm
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.


def index(request):
    try:
        desenvolvedor = Desenvolvedor.objects.get(id=request.session['desenvolvedor_id'])
        todos_projetos = desenvolvedor.projetos.all
        return render(request, 'analise_de_requisitos/index.html',
                      {'desenvolvedor': desenvolvedor, 'todos_projetos': todos_projetos})
    except KeyError:
        messages.warning(request, 'Desenvolvedor não logado')
        return redirect('desenvolvedor_index')


def show(request, ar_id):
    request.session['ar_id'] = ar_id
    analise_de_requisito = AnaliseDeRequisitos.objects.get(id=ar_id)
    equipe = analise_de_requisito.desenvolvedores.all()
    return render(request, 'analise_de_requisitos/show.html',
                  {'analise_de_requisito': analise_de_requisito, 'equipe': equipe})


def new(request):
    form = AnaliseDeRequisitosForm()
    return render(request, 'analise_de_requisitos/new.html', {'form': form})


def create(request):
    form = AnaliseDeRequisitosForm(request.POST)
    if form.is_valid():
        novo_projeto = AnaliseDeRequisitos(nome=request.POST['nome'], descricao=request.POST['descricao'])
        novo_projeto.save()
        desenvolvedor_atual = Desenvolvedor.objects.get(id=request.session['desenvolvedor_id'])
        nova_equipe = Equipe(dev_id=desenvolvedor_atual, ar_id=novo_projeto)
        nova_equipe.save()
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
        messages.warning(request, 'Formulário inválido')
        return redirect('ar_edit')


def delete(request):
    projeto_atual = AnaliseDeRequisitos.objects.get(id=request.session['ar_id'])
    projeto_atual.delete()
    del request.session['ar_id']
    messages.success(request, 'Projeto apagado com sucesso')
    return redirect('ar_index')


def remove_dev(request, dev_id):
    relacao = Equipe.objects.get(dev_id=dev_id, ar_id=request.session['ar_id'])
    relacao.delete()
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
    equipe_atualizada = Equipe(dev_id=novo_desenvolvedor, ar_id=projeto_atual)
    equipe_atualizada.save()
    messages.success(request, 'Desenvolvedor adicionado ao projeto com sucesso')
    return redirect('ar_show', request.session['ar_id'])

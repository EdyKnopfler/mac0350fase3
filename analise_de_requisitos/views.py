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
        return render(request, 'analise_de_requisitos/index.html', {'desenvolvedor': desenvolvedor, 'todos_projetos': todos_projetos})
    except KeyError:
        messages.warning(request, 'Desenvolvedor não logado')
        return redirect('desenvolvedor_index')


def show(request, ar_id):
    request.session['ar_id'] = ar_id
    analise_de_requisito = AnaliseDeRequisitos.objects.get(id=ar_id)
    return render(request, 'analise_de_requisitos/show.html', {'analise_de_requisito': analise_de_requisito})

def new(request):
    form = AnaliseDeRequisitosForm()
    return render(request, 'analise_de_requisitos/new.html', {'form': form})

def create(request):
    form = AnaliseDeRequisitosForm(request.POST)
    if form.is_valid():
        novo_projeto = AnaliseDeRequisitos(nome=request.POST['nome'], descricao=request.POST['descricao'])
        novo_projeto.save()
        desenvolvedor_atual = Desenvolvedor.objects.get(id=request.session['desenvolvedor_id'])
        nova_equipe = Equipe(desenvolvedor=desenvolvedor_atual, analise_de_requisito=novo_projeto)
        nova_equipe.save()
        messages.success(request, 'Projeto criado com sucesso')
    else:
        messages.warning(request, 'Falha na criação do Projeto')
    return redirect('ar_index')

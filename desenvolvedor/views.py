# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from desenvolvedor.models import Desenvolvedor
from .forms import RegistroForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction


# Create your views here.


def index(request):
    if 'desenvolvedor_id' in request.session:
        return redirect('ar_index')
    else:
        return render(request, 'index.html')


def enter(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def new(request):
    form = RegistroForm()
    return render(request, 'new.html', {'form': form})


def create(request):
    form = RegistroForm(request.POST)
    if form.is_valid():
        novo_desenvolvedor = Desenvolvedor(nome=request.POST['nome'], email=request.POST['email'],
                                           senha=request.POST['senha'])
        novo_desenvolvedor.save()
        messages.success(request, 'Desenvolvedor criado com sucesso')
    else:
        messages.warning(request, 'Formulário inválido')
    return redirect('desenvolvedor_index')


def login(request):
    try:
        desenvolvedor_existente = Desenvolvedor.objects.get(email=request.POST['email'])
        if desenvolvedor_existente.email == request.POST['email'] and desenvolvedor_existente.senha == request.POST[
            'senha']:
            request.session['desenvolvedor_id'] = desenvolvedor_existente.id
            return redirect('ar_index')
        else:
            messages.warning(request, 'Email ou Senha inválidos. Verifique os dados e tente novamente')
    except Desenvolvedor.DoesNotExist:
        messages.warning(request, 'Desenvolvedor inexistente')
    return redirect('desenvolvedor_index')


def logout(request):
    request.session.flush()
    messages.success(request, 'Desenvolvedor saiu com sucesso')
    return redirect('desenvolvedor_index')


def edit(request):
    antigo_desenvolvedor = Desenvolvedor.objects.get(id=request.session['desenvolvedor_id'])
    form = RegistroForm(instance=antigo_desenvolvedor)
    return render(request, 'edit.html', {'form': form})


def update(request):
    antigo_desenvolvedor = Desenvolvedor.objects.get(id=request.session['desenvolvedor_id'])
    desenvolvedor_atualizado = RegistroForm(request.POST, instance=antigo_desenvolvedor)
    if desenvolvedor_atualizado.is_valid():
        desenvolvedor_atualizado.save()
        messages.success(request, 'Desenvolvedor atualizado com sucesso')
    else:
        messages.warning(request, 'Formulário inválido')
    return redirect('desenvolvedor_index')


def delete(request):
    with transaction.atomic():
        desenvolvedor_atual = Desenvolvedor.objects.get(id=request.session['desenvolvedor_id'])
        desenvolvedor_atual.delete()
        messages.success(request, 'Desenvolvedor apagado com sucesso')
    return redirect('desenvolvedor_logout')

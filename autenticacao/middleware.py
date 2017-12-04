# -*- coding: utf-8 -*-

from django.contrib import messages
from django.shortcuts import redirect
from django.db import connection


def autenticacao_middleware(get_response):
    def middleware(request):
        if not (
                request.path == '/' or request.path == '/login/' or request.path == '/new/' or request.path == '/create/' or request.path == '/enter/') and 'desenvolvedor_id' not in request.session:
            messages.warning(request, 'Por favor, faça login.')
            return redirect('/')

        response = get_response(request)
        return response

    return middleware


def consultas_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        print("\n\nQUERIES")
        print(connection.queries)
        return response

    return middleware

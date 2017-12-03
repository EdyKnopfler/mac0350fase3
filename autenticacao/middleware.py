from django.contrib import messages
from django.shortcuts import redirect

def autenticacao_middleware(get_response):

    def middleware(request):
        if not (request.path == '/' or request.path == '/login/' or \
                request.path == '/new/' or request.path == '/create/') and \
           not 'desenvolvedor_id' in request.session:
            messages.warning(request, 'Por favor, faça login.')
            return redirect('/')
            
        response = get_response(request)
        return response

    return middleware

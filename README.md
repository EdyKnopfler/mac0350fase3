CRIAR E POVOAR O BANCO DE DADOS POR SCRIPTS

1. Em mac0350fase3/projeto/settings.py, configurar o banco de dados

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'analise_requisitos',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

2. Criar o banco de dados no PostgreSQL

python3 criar_bd.py usuário senha [nome_bd]
    nome_bd: opcional. (Default: analise_requisitos)

3. Povoar banco de dados

python3 povoar_bd.py usuário senha [nome_bd]
    nome_bd: opcional. (Default: analise_requisitos)


CRIAR E POVOAR O BANCO DE DADOS MANUALMENTE

1. Em mac0350fase3/projeto/settings.py, configurar o banco de dados

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'analise_requisitos',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

2. Criar o banco de dados no PostgreSQL

-- OWNER = coloque o nome do seu usuário, sem aspas

CREATE DATABASE analise_requisitos
  WITH OWNER = usuario
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'pt_BR.UTF-8'
       LC_CTYPE = 'pt_BR.UTF-8'
       CONNECTION LIMIT = -1;

ou

CREATE DATABASE analise_requisitos
  WITH OWNER = usuario;
       
3. Criar as tabelas geradas pelo Django

python3 manage.py makemigrations
python3 manage.py migrate

4. Povoar banco de dados

python3 povoar_bd.py usuário senha [nome_bd]
    nome_bd: opcional. (Default: analise_requisitos)

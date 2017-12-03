1. Criar o banco de dados no PostgreSQL:

-- OWNER = coloque o nome do seu usuário, sem aspas

CREATE DATABASE analise_requisitos
  WITH OWNER = nome_do_usuario
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'pt_BR.UTF-8'
       LC_CTYPE = 'pt_BR.UTF-8'
       CONNECTION LIMIT = -1;
       
2. Em mac0350fase3/projeto/settings.py, configurar o banco de dados:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'analise_requisitos',
        'USER': 'nome_do_usuario',
        'PASSWORD': '........',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

3. Criar as tabelas geradas pelo Django:

$ python3 manage.py migrate

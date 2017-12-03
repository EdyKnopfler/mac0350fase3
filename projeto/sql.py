# BASEADO EM: http://initd.org/psycopg/articles/2012/10/01/prepared-statements-psycopg/

from django.db import connection

def preparar(nome, sql):
    cursor = connection.cursor()
    cursor.execute('prepare ' + nome + ' as ' + sql + ';')
    return cursor

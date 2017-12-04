from django.db import connection

def executar_consulta(consulta, params):
    cursor = connection.cursor()
    cursor.execute(consulta, params)
    return cursor

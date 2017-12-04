from projeto.sql import executar_consulta

def atividade_join_requisito(id_ativ):
    cursor = executar_consulta("""
        SELECT a.id, a.descricao, a.data_inicio, a.data_fim, a.prazo, a.req_id_id, r.ar_id_id
        FROM atividade a, requisito r
        WHERE a.req_id_id = r.id AND a.id = %s;
    """, (id_ativ,))
    tupla = cursor.fetchone()
    dados = {'id': tupla[0], 'descricao': tupla[1], 'data_inicio': tupla[2], 'data_fim': tupla[3], 
             'prazo': tupla[4], 'req_id': tupla[5], 'ar_id': tupla[6]}
    cursor.close()
    return dados

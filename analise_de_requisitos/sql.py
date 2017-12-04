from projeto.sql import executar_consulta
from django.db import connection

def projetos_desenvolvedor(id_desenv):
    return executar_consulta("""
        SELECT ar.id, ar.nome 
        FROM analise_de_requisitos ar, equipe e
        WHERE 
            e.ar_id_id = ar.id AND
            e.dev_id_id = %s
        ORDER BY ar.nome;
    """, (id_desenv,))

def atividades_desenvolvedor(id_desenv):
    return executar_consulta("""
        SELECT id, descricao, prazo
        FROM atividade
        WHERE dev_id_id = %s
        ORDER BY descricao;
    """, (id_desenv,))

def desenvolvedores_projeto(id_proj):
    return executar_consulta("""
        SELECT d.id, d.nome, d.email
        FROM desenvolvedor d, equipe e
        WHERE
            e.dev_id_id = d.id AND
            e.ar_id_id = %s
    """, (id_proj,))

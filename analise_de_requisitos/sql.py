from projeto.sql import preparar

class AnalisesRequisitosSQL:

    def __init__(self):
        self.cursor_projetos = None
        self.cursor_atividades = None
        self.cursor_desenvolvedores = None

    def projetos_desenvolvedor(self, id_desenv):
        if self.cursor_projetos == None:
            self.cursor_projetos = preparar('projetos_desenvolvedor', """
                SELECT ar.id, ar.nome 
                FROM analise_de_requisitos ar, equipe e
                WHERE 
                    e.ar_id_id = ar.id AND
                    e.dev_id_id = $1
                ORDER BY ar.nome;
            """)
        self.cursor_projetos.execute('execute projetos_desenvolvedor (%s);', (id_desenv,))

    def atividades_desenvolvedor(self, id_desenv):
        if self.cursor_atividades == None:
            self.cursor_atividades = preparar('atividades_desenvolvedor', """
                SELECT id, descricao, prazo
                FROM atividade
                WHERE dev_id_id = $1
                ORDER BY descricao;
            """)
        self.cursor_atividades.execute('execute atividades_desenvolvedor (%s);', (id_desenv,))
    
    def desenvolvedores_projeto(self, id_proj):
        if self.cursor_desenvolvedores == None:
            self.cursor_desenvolvedores = preparar('desenvolvedores_projeto', """
                SELECT d.id, d.nome, d.email
                FROM desenvolvedor d, equipe e
                WHERE
                    e.dev_id_id = d.id AND
                    e.ar_id_id = $1
            """)
        self.cursor_desenvolvedores.execute('execute desenvolvedores_projeto (%s);', (id_proj,))

sql = AnalisesRequisitosSQL()

-- Consultas geradas pelo Django, exceto onde assinaladas
-- Parâmetros representados por $1, $2, ..., $n

-- Registro de desenvolvedor

SELECT (1) AS "a" 
FROM "desenvolvedor" 
WHERE "desenvolvedor"."email" = $1 
LIMIT 1;

-- Login 

SELECT "desenvolvedor"."id", "desenvolvedor"."nome", "desenvolvedor"."email", "desenvolvedor"."senha" 
FROM "desenvolvedor" 
WHERE "desenvolvedor"."email" = $1;

INSERT INTO "desenvolvedor" ("nome", "email", "senha") VALUES ($1, $2, $3) 
RETURNING "desenvolvedor"."id";

-- Editando desenvolvedor

SELECT "desenvolvedor"."id", "desenvolvedor"."nome", "desenvolvedor"."email", "desenvolvedor"."senha" 
FROM "desenvolvedor" 
WHERE "desenvolvedor"."id" = $3;

SELECT (1) AS "a" FROM "desenvolvedor" 
WHERE ("desenvolvedor"."email" = $1 AND NOT ("desenvolvedor"."id" = $2)) 
LIMIT 1;

UPDATE "desenvolvedor" 
SET "nome" = $1, "email" = $2, "senha" = $3 
WHERE "desenvolvedor"."id" = $4;

-- Apagando desenvolvedor

SELECT "desenvolvedor"."id", "desenvolvedor"."nome", "desenvolvedor"."email", "desenvolvedor"."senha" 
FROM "desenvolvedor" 
WHERE "desenvolvedor"."id" = $1;

DELETE FROM "equipe" 
WHERE "equipe"."dev_id_id" IN ($1);

DELETE FROM "atividade" 
WHERE "atividade"."dev_id_id" IN ($1);

DELETE FROM "desenvolvedor" 
WHERE "desenvolvedor"."id" IN ($1)

-- Formulário para editar a conta

SELECT "desenvolvedor"."id", "desenvolvedor"."nome", "desenvolvedor"."email", "desenvolvedor"."senha" 
FROM "desenvolvedor" 
WHERE "desenvolvedor"."id" = $1;

-- Página do desenvolvedor: listagem de projetos de análise de requisitos e atividades
-- Consultas em analise_de_requisitos/sql.py

SELECT ar.id, ar.nome 
FROM analise_de_requisitos ar, equipe e
WHERE 
    e.ar_id_id = ar.id AND
    e.dev_id_id = $1
ORDER BY ar.nome;

SELECT id, descricao, prazo
FROM atividade
WHERE dev_id_id = $1
ORDER BY descricao;

-- Mostrando projeto

SELECT "analise_de_requisitos"."id", "analise_de_requisitos"."nome", "analise_de_requisitos"."descricao" 
FROM "analise_de_requisitos" 
WHERE "analise_de_requisitos"."id" = $1;

SELECT "requisito"."id", "requisito"."tipo", "requisito"."nome", "requisito"."detalhes", "requisito"."ar_id_id" 
FROM "requisito" 
WHERE "requisito"."ar_id_id" = $1;

SELECT d.id, d.nome, d.email  -- consulta em analise_de_requisitos/sql.py
FROM desenvolvedor d, equipe e
WHERE
    e.dev_id_id = d.id AND
    e.ar_id_id = $1

-- Inserindo projeto

INSERT INTO "analise_de_requisitos" ("nome", "descricao") VALUES ($1, $2) 
RETURNING "analise_de_requisitos"."id";

INSERT INTO "equipe" ("dev_id_id", "ar_id_id") VALUES ($1, $2) 
RETURNING "equipe"."id";

-- Mostrando formulário de edição do projeto

SELECT "analise_de_requisitos"."id", "analise_de_requisitos"."nome", "analise_de_requisitos"."descricao" 
FROM "analise_de_requisitos" 
WHERE "analise_de_requisitos"."id" = $1;

-- Editando projeto

SELECT "analise_de_requisitos"."id", "analise_de_requisitos"."nome", "analise_de_requisitos"."descricao" 
FROM "analise_de_requisitos" 
WHERE "analise_de_requisitos"."id" = $1;

UPDATE "analise_de_requisitos" 
SET "nome" = $1, "descricao" = $2 
WHERE "analise_de_requisitos"."id" = $3;

-- Apagando projeto

SELECT "analise_de_requisitos"."id", "analise_de_requisitos"."nome", "analise_de_requisitos"."descricao" 
FROM "analise_de_requisitos" 
WHERE "analise_de_requisitos"."id" = $1;

SELECT "requisito"."id", "requisito"."tipo", "requisito"."nome", "requisito"."detalhes", "requisito"."ar_id_id" 
FROM "requisito" 
WHERE "requisito"."ar_id_id" IN ($1);

DELETE FROM "equipe" 
WHERE "equipe"."ar_id_id" IN ($1);

DELETE FROM "analise_de_requisitos" 
WHERE "analise_de_requisitos"."id" IN ($1);

-- Criando requisito

SELECT "analise_de_requisitos"."id", "analise_de_requisitos"."nome", "analise_de_requisitos"."descricao" 
FROM "analise_de_requisitos" 
WHERE "analise_de_requisitos"."id" = $1;

INSERT INTO "requisito" ("tipo", "nome", "detalhes", "ar_id_id")  VALUES ($1, $2, $3, $4) 
RETURNING "requisito"."id";

-- Mostrando requisito

SELECT "requisito"."id", "requisito"."tipo", "requisito"."nome", "requisito"."detalhes", "requisito"."ar_id_id" 
FROM "requisito" 
WHERE "requisito"."id" = $1;

SELECT "analise_de_requisitos"."id", "analise_de_requisitos"."nome", "analise_de_requisitos"."descricao" 
FROM "analise_de_requisitos" 
WHERE "analise_de_requisitos"."id" = $1;

SELECT "atividade"."id", "atividade"."dev_id_id", "atividade"."req_id_id", "atividade"."descricao", "atividade"."data_inicio", "atividade"."data_fim", "atividade"."prazo" 
FROM "atividade" 
WHERE "atividade"."req_id_id" = $1;

-- Mostrando formulário de edição de requisito

SELECT "requisito"."id", "requisito"."tipo", "requisito"."nome", "requisito"."detalhes", "requisito"."ar_id_id" 
FROM "requisito" 
WHERE "requisito"."id" = $1;

-- Atualizando requisito

SELECT "requisito"."id", "requisito"."tipo", "requisito"."nome", "requisito"."detalhes", "requisito"."ar_id_id" 
FROM "requisito" 
WHERE "requisito"."id" = $1;

UPDATE "requisito" 
SET "tipo" = $1, "nome" = $2, "detalhes" = $3, "ar_id_id" = $4 
WHERE "requisito"."id" = $5;

-- Apagando requisito

SELECT "requisito"."id", "requisito"."tipo", "requisito"."nome", "requisito"."detalhes", "requisito"."ar_id_id" 
FROM "requisito" 
WHERE "requisito"."id" = $1;

DELETE FROM "atividade" 
WHERE "atividade"."req_id_id" IN ($1);

DELETE FROM "requisito" WHERE "requisito"."id" IN ($1);

-- Criando atividade

INSERT INTO "atividade" ("dev_id_id", "req_id_id", "descricao", "data_inicio", "data_fim", "prazo") 
VALUES ($1, $2, $3, $4, $5, $6) RETURNING "atividade"."id";

-- Formulário para editar atividade
-- consulta em atividade/sql.py

SELECT a.id, a.descricao, a.data_inicio, a.data_fim, a.prazo, a.req_id_id, r.ar_id_id
FROM atividade a, requisito r
WHERE a.req_id_id = r.id AND a.id = %s;

-- Editar atividade

SELECT "atividade"."id", "atividade"."dev_id_id", "atividade"."req_id_id", "atividade"."descricao", 
       "atividade"."data_inicio", "atividade"."data_fim", "atividade"."prazo" 
FROM "atividade" 
WHERE "atividade"."id" = $1;

UPDATE "atividade" 
SET "dev_id_id" = $1, "req_id_id" = $2, "descricao" = $3, "data_inicio" = $4::date, 
    "data_fim" = $5::date, "prazo" = $6::date 
WHERE "atividade"."id" = $7

-- Apagar atividade

SELECT "atividade"."id", "atividade"."dev_id_id", "atividade"."req_id_id", "atividade"."descricao", "atividade"."data_inicio", "atividade"."data_fim", "atividade"."prazo" FROM "atividade" WHERE "atividade"."id" = $1;

DELETE FROM "atividade" WHERE "atividade"."id" IN (1);

-- Seleção de desenvolvedor para a equipe do projeto

SELECT "desenvolvedor"."id", "desenvolvedor"."nome", "desenvolvedor"."email", "desenvolvedor"."senha" 
FROM "desenvolvedor" 
WHERE NOT ("desenvolvedor"."id" IN (
    SELECT U0."dev_id_id" AS Col1 FROM "equipe" U0 WHERE U0."ar_id_id" = $1));

-- Adicionando desenvolvedor à equipe

INSERT INTO "equipe" ("dev_id_id", "ar_id_id") VALUES ($1, $2) RETURNING "equipe"."id";

-- Removendo desenvolvedor da equipe

SELECT "equipe"."id", "equipe"."dev_id_id", "equipe"."ar_id_id" 
FROM "equipe" 
WHERE ("equipe"."dev_id_id" = 2 AND "equipe"."ar_id_id" = $1;

DELETE FROM "equipe" WHERE "equipe"."id" IN ($1);



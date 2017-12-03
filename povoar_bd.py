#!/usr/bin python3
# -*- coding: utf-8 -*-

from sys import argv
import psycopg2

def povoar_desenvolvedor():
    #(nome, email, senha)
    desenvolvedores = [
        ('Rafael Alves Dias', 'rafaeldias@mac0350.com', 'Wj93279w%*9i'),
        ('Matheus Fernandes', 'matheusfernandes@mac0350.com', 'I1n3931%0JdA'),
        ('Alice Sousa', 'alicesousa@mac0350.com', 'mY187L03$HwC'),
        ('Vinicius Rocha', 'viniciusrocha@mac0350.com', '03Ze3^1%4ITa'),
        ('Douglas Rodrigues', 'douglasrodrigues@mac0350.com', '6r5T5!8V4vAI'),
        ('Gabriela Correia', 'gabrielacorreia@mac0350.com', 'A3p9#6!55%1Q'),
        ('Gabriela Oliveira', 'gabrielaoliveira@mac0350.com', '84Dx4h^3h9sG'),
        ('Brenda Cunha', 'brendacunha@mac0350.com', '8y83LV6&3eB7'),
        ('Fábio Almeida Santos', 'fabiosantos@mac0350.com', '4C6Mb6%09qTM'),
        ('Carolina Silva', 'carolinasilva@mac0350.com', '01*Hro0529TF')]

    cur.executemany("INSERT INTO desenvolvedor(nome, email, senha) VALUES (%s, %s, %s);", desenvolvedores)

def povoar_ar():
    #(nome, descricao)
    analise_requisitos = [
        ('Laboratório Santa Maria', 'Criação de um software de armazenamento e recuperação de dados de pacientes para o diagnóstico molecular.')]

    cur.executemany("INSERT INTO analise_de_requisitos(nome, descricao) VALUES (%s, %s);", analise_requisitos)

def povoar_equipe():
    #(dev_id, ar_id)
    equipes = [
        ('2', '1'),
        ('3', '1'),
        ('7', '1'),
        ('5', '1')]

    cur.executemany("INSERT INTO equipe(dev_id_id, ar_id_id) VALUES (%s, %s);", equipes)

def povoar_requisito():
    #(nome, tipo, detalhes, ar_id)
    requisitos = [
        ('Paciente', 'Dado', 'Todas as pessoas que são tratadas no laboratório devem possuir um cadastro, contendo: nome, data de nascimento, situação civil, RG, CPF, endereço, complemento, CEP, email, telefone.', '1'),
        ('Diagnóstico Molecular', 'Dado', 'Representa o diagnóstico de uma doença hereditária. As informações são: causa molecular da doença, alguma deleção de genes ou pedaços de cromossomos, variantes diferentes do que o encontrado na população saudável.', '1'),
        ('Cadastro de informações do paciente', 'Funcional', 'Qualquer funcionário pode fazer o cadastro e alteração das informações dos pacientes.', '1'),
        ('Agendamento de máquina', 'Funcional', 'Qualquer funcionário pode agendar o uso das máquinas. Um mesmo funcionário não pode agendar mais de uma máquina ao mesmo tempo. Cada tipo de máquina pode ter um tempo limite de uso.', '1')]

    cur.executemany("INSERT INTO requisito(nome, tipo, detalhes, ar_id_id) VALUES (%s, %s, %s, %s);", requisitos)

def povoar_atividade():
    #(dev_id, req_id, descricao, dt_inicio, dt_fim, prazo)
    atividades = [
        ('2', '1', 'Implementação da tabela de paciente no banco de dados.', '2017-10-23', None, '2017-10-26'),
        ('7', '4', 'Implementação da função de restrição de agendamento de uma única máquina ao mesmo tempo.', '2017-10-20', None, '2017-10-25'),
        ('3', '4', 'Implementação do tipo de máquina para tempo de uso.', '2017-10-20', '2017-10-21', '2017-10-22')]

    cur.executemany("INSERT INTO atividade(dev_id_id, req_id_id, descricao, data_inicio, data_fim, prazo) VALUES (%s, %s, %s, %s, %s, %s);", atividades)

def povoar_bd(conn):
    povoar_desenvolvedor()
    povoar_ar()
    conn.commit()
    povoar_equipe()
    povoar_requisito()
    povoar_atividade()

if (len(argv) < 2):
    print("./povoar_bd.py usuário senha")
    exit(0)

user = argv[1]
password = argv[2]

try:
    conn = psycopg2.connect("dbname='database' user={} host='localhost' password={}".format(user, password)) 
except:
    print("ERRO: não foi possível conectar ao banco de dados.")
    exit(0)

cur = conn.cursor()

povoar_bd(conn)

cur.close()
conn.commit()
conn.close()

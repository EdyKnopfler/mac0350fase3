#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psycopg2
from sys import argv
import subprocess

def execute_migration():
    cmd_makemigrations = ['python3', 'manage.py', 'makemigrations']
    cmd_migrate = ['python3', 'manage.py', 'migrate']

    subprocess.run(cmd_makemigrations)
    subprocess.run(cmd_migrate)

def create_database(cur, user, dbname):
    try:
        sql = "CREATE DATABASE {} WITH OWNER = {} ENCODING = 'UTF8' TABLESPACE = pg_default LC_COLLATE = 'pt_BR.UTF-8' LC_CTYPE = 'pt_BR.UTF-8' CONNECTION LIMIT = -1".format(dbname, user)
        cur.execute(sql)
    except:
        sql = "CREATE DATABASE {} WITH OWNER = {}".format(dbname, user)
        cur.execute(sql)
    finally:
        return

def get_options(argv):
    user = argv[1]
    password = argv[2]
    if (len(argv) > 3):
        bdname = argv[3]
    else:
        bdname = 'analise_requisitos'

    return (user, password, bdname)

def main():
    if (len(argv) < 2):
        print("./criar_bd.py usuário senha [nome_bd]")
        print("\tnome_bd: opcional. (Default: analise_requisitos)")
        exit(0)

    user, password, dbname = get_options(argv)

    try:
        conn = psycopg2.connect("user={} host='localhost' password={}".format(user, password)) 
    except:
        print("ERRO: não foi possível conectar ao usuário.")
        exit(0)

    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT) 
    cur = conn.cursor()

    create_database(cur, user, dbname)
    execute_migration()

    cur.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()

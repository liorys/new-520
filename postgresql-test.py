#!/usr/bin/python3
# pip3 install psycopg2



import psycopg2

con = psycopg2.connect('host=localhost dbname=projeto\
                            user=admin password=4linux port=5432')
cur = con.cursor()  

def inserir(nome,idade,telefone,email):
    try:

        cur.execute("insert into pessoas(nome,email,telefone,idade) values ({},{},{},{})".format(nome,email,telefone,idade))
        con.commit()

    except Exception as e:
        print('Err:{}'.format(e))


nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
tel = input('Digite o telefone : ')
email = input('Digite o email: ')   



inserir(nome,idade,tel,email)
cur.execute('select * from pessoas')
tabela = cur.fetchall()

for x in tabela:
    print('''
        Nome: \t{}\t\tid:{}
        Idade: \t{}
        Telefone: \t{}
        E-mail: \t{}
'''.format(x[1],x[0],x[3],x[4],x[2]))








exit()















try:
    con = psycopg2.connect('host=localhost dbname=projeto\
                        user=admin password=4linux port=5432')
    cur = con.cursor()
    # cur.execute("insert into pessoas(nome,email,telefone,idade) values ('juninho','juninho@juninho','00000',10)")
    cur.execute('select * from pessoas')# seleciona toda a tabela e armazena em uma variavel
    tabela = cur.fetchall()# fetchall seleciona todas as informacoes da tabela
    # tabela = cur.fetchone()# fetchone seleciona a primeira informacao da tabela
    # print(tabela)
    # print('Connection OK')
    con.commit()# commite para executar

    for x in tabela:
        print('''
            Nome: \t{}\t\tid:{}
            Idade: \t{}
            Telefone: \t{}
            E-mail: \t{}
'''.format(x[1],x[0],x[3],x[4],x[2]))


except Exception as e:
    print('Err:{}'.format(e))

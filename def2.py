#!/usr/bin/python3

# args usado para quando nao se sabe o numero de argumetos
# def boas_vindas(*args): 
#     for arg in args:
#         print('Ola {} seja bem vindo(a)'.format(arg))

# boas_vindas('fabio','maria','joao')

# kargs transforma os parametros em dicionario

# def boas_vindas(**kargs): 
#     print('Bem vindo {} idade {}'\
#     .format(kargs['nome'],kargs['idade']))

# boas_vindas(nome='fabio',sobrenome='fugiyama',idade='19019')



def total(**kargs):
    return kargs['qtd']*kargs['preco']
    
print(total(qtd=51,preco=2.0))



# print(result)
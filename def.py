#!/usr/bin/python3

import pdb

# pdb.set_trace()# Debug python

####### Funcoes ###########

# def boas_vindas(nome='maria',idade='37'): # parametros default
#     return('ola {} voce tem {} anos'.format(nome,idade))


# def soma(x,y):
#     return x+y

# a = boas_vindas('fabio')
# b = soma(7,19)
# print(b)
# print(a)

# print(soma(3,2))# print funcao soma

# print(boas_vindas(idade=76,nome='fabio'))
# boas_vindas() # sem argumentos mostra o parametro DEFAULT


# newlist=[]

# with open ('frutas.txt','r') as arquivo:
#     arquivo.readlines()
#     var = arquivo


# print(type(var))

########### DEF PAR OU IMPAR ############

# def par_impar(parametro):
#     if parametro %2 ==0:
#         return('o numero é PAR')
#     else:
#         return('o numero é IMPAR')


# while True:
#     entrada = input('Digite um numero ou S para sair: ')
#     if entrada.lower() =='s':
#         break
#     elif entrada.lower() != 's':
#         try:
#             entrada = entrada = int(entrada)
#         except Exception as e:
#             # print('Erro: {}'.format(e))
#             continue
#         print(par_impar(entrada))
 
        

######## Def manipular arquivo ############## 

def manipular_arq(nome,modo='r',conteudo=None):
    if modo == 'r':
        with open(nome,modo) as arquivo:
            return arquivo.readlines()
    elif modo == 'a':
        with open (nome,modo) as arquivo:
            arquivo.write(conteudo +'\n')
            return True



a = manipular_arq('nomes.txt','r')
b = manipular_arq('frutas.txt','a','abacateeeee')
c = manipular_arq('frutas.txt','r')
print(c)
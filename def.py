#!/usr/bin/python3

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

def par_impar(parametro):
    if parametro %2 ==0:
        return('o numero é PAR')
    else:
        return('o numero é IMPAR')


while True:
    entrada = input('Digite um numero ou S para sair: ')
    if entrada.lower() =='s':
        break
    if entrada.lower() != 's':
        continue
    else:
        entrada = int(entrada)
        print(par_impar(entrada))





#!/usr/bin/python3

nome = ['fabio','carla','maria','joseee']


############### METODOS DE STRING ###########
# nome.tittle()# altera a primeira letra para Maiusculo
# nome.strip()# retira os espacos
# nome.rstrip()# retira os espacos a direita
# nome.lstrip()# retora os espacos a esquerda

############### METODOS E PARAMETROS EM LISTA ############
# nome.reverse()# Metodo para inverter a lista
# nome.index(fabio)# Tras a posicao do primeiro nome na lista
# nome.append(['marta','goku'])# insere no final da lista
# nome.insert(0,'goku')# insere na posicao desejada
# nome.pop()# retira o ultimo da lista, ou o selecionado nome.pop(2)
# nome.remove('fabio')# remove item selecionado
# nome.sort()# ordena lista de forma numerica interna no python - ord(J) -  chr(74)
# nome.count('fabio')# conta quantos nomes fabio tem na lista
# nome.split(# separa o utilizando espaco como separador
# len(nome)# verifica o tamanho da lista
# set(nome)# mostra conteudos nao duplicados na lista, list(set(nome)) mostra em formato lista
# nome[1] = teste# alterar valor em lista
# nome.replace('\n','-{}\n'.format(cont))# substitui intem da lista

################ PRINT SEM PULAR LINHA ##################
# print('fabio','maria', sep'.')# altera o separador para . (ponto)
# print('fabio','maria', sep'.',end='\n\n')# altera o separador para . e da 2 enter
# print('fabio','maria', end='')# nao pula linha na saida do print


# nome = [nomes.title() for nomes in nome]#list compression cria uma \
# copia da propria lista formatada

# print('sim' if nome == ' daniel else 'nao') #ifternario


########### EXEMPLO LISTA COM LETRAS ###################

# letras=[]
# maiusculas=[]

# for x in range(97, 97 + 27):
#     letras.append(chr(x))
# print(letras,end='\n\n')

# for y in range(65,90):
#     maiusculas.append(chr(y))
# print(maiusculas)

# exit()


# numeros = list(range(40,100))# cria lista de numeros de 40 a 100

# print(nome[2])
# nomes2 = nome[2:]
# print(nomes2)
# nome.append(['marta','goku']) insere no final da lista
# nome.insert(0,'goku')#insere na posicao desejada


# print(nome)
# nome.insert(0,'goku')#insere na posicao desejada
# print(nome)
# nome.pop()#retira o ultimo da lista
# print(nome)
# nome.remove('goku')#remove o item desejadoo
# print(nome)
# print(nome[-1][1]) # print lista dentro de lista
# print(len(nome))
# print(numeros)

###############################################
############## DICIONARIO #####################
###############################################

pessoa = {'nome':'fabio','endereco':'rua x','email':'fabio@fabiooo'}
pessoa.keys()# retorna somente as chaves do docionario
pessoa.values()# retorna somemte os valores

############### METODOS E PARAMETROS EM DICIONARIO #######

# PERCORRER LISTANDO SOMENTE AS CHAVES
# for x in pessoa.keys():
#     print(x)

# PERCORRER LISTANDO SOMENTE OS VALORES
# for x in pessoa.values():
#     print(x)

# PERCORRER LISTANDO CHAVE E VALOR
# for x, y in pessoa.items():
#      print(x,y)

# PESQUISA VALOR DA CHAVE NO DICIONARIO
# print(pessoa.get('aksld','NONE'))# 0 informacao retornada no caso da inexistencia da chave

# REMOVE ELEMENTO DO DICIONARIO
# del pessoa['nome']
print(pessoa)

exit()


####### LISTA COM DICIONARIO #################

from pprint import pprint

pessoas =  [
    {'nome':'fabio','idade':'27'},
    {'nome':'joao','idade':'45'},
    {'nome':'maria','idade':'45'},
    {'nome':'pedro','idade':'20'},

]

print(type(pessoas))
print(pessoas[0])# retorna a o indice 0 da lista
print(type(pessoas[0]))# verifica o que e o indice 0
print(pessoas[0]['idade'])# retorna somente idade
print(type(pessoas[0]['idade']))

pprint(pessoas)# utiliza library pprint,torna saida mais legivel




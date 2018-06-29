#!/usr/bin/python3
from pprint import pprint
frutas = [
{'nome':'laranja','preco':2.0,'qtd':10},
{'nome':'abacaxii','preco':5.55,'qtd':20},
{'nome':'uva','preco':4.5,'qtd':2},
{'nome':'melancia','preco':7.0,'qtd':4},
{'nome':'morango','preco':5.0,'qtd':11}

]
# frutas2 = []
#####
#######
# # retorna novo preco das frutas
# for fruta in frutas:
#     fruta['preco'] += fruta['preco'] * 0.1 # acrecimo de 10%
#     # fruta['preco'] = fruta['preco'] + 0.5
#     frutas2.append(fruta)
#    # print(fruta)

# pprint(frutas2)

soma = 0
for x in frutas:
    soma += x['preco'] * x['qtd']
print('Total: {:.2f}'.format(soma))













# select = input('Digite o nome da fruta: ')
# print( pera in frutas['nome'])

# if select in frutas[]:
#     print('a fruta existe')
# else:
#     print('nao existe')
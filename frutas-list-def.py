#!/usr/bin/python3

from pprint import pprint


frutas = [
        {'nome':'pera','preco':'1.0','qtd':'10'},
        {'nome':'uva','preco':'2.0','qtd':'20'},
        {'nome':'abacaxi','preco':'3.0','qtd':'30'},
        {'nome': 'morango', 'preco': '4.0', 'qtd': '40'},
        {'nome': 'kiwi', 'preco': '5.0', 'qtd': '50'},

    ]

def buscafruta(frutasearch):

    for fruta in frutas:
        fruta['nome']
        if fruta['nome'] == frutasearch:
            return ('A fruta existe na lista.')
            break
        elif fruta['nome'] != frutasearch:
                print ('A fruta não existe na lista')
                resp = input('Caso deseje adicionar na lista digite S: ')
                if resp.lower() == 's':
                    frutanova = input('Qual o nome da nova fruta ?')
                    preconova = float(input('Qual o valor da nova fruta ?'))
                    qtdnova = int(input('Qual a quantidade deseja inserir? '))
                    frutas.append({'nome':frutanova,'preco':preconova,'qtd':qtdnova})
                    print('Nova lista de frutas \n\n',frutas)
                    print('Adicionado com sucesso')




while True:
    select = input('Digite o nome da fruta para pesquisar ou x para sair ')
    if select.lower() == 'x':
        print('Saindo do programa . . .')
        break
    print(buscafruta(select))









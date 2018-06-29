#!/usr/bin/python3

######### ESCREVE EM ARQUIVO ###########
# arquivo = open('frutas.txt', 'a')
# arquivo.write('abacaxi')
# arquivo.close()

######### ESCREVE EM ARQUIVO SEM PRECISAR FEXAR O ARQUIVO ###########
# modo 'a' cria arquivo caso nao exista
# mode 'w' sobrescreve os arquivos existentes
# modo 'r' da somente permissao de leitura
# modeo '+' possibilita outra funcao 'r+' possibilita read write
# arquivo.read() le o arqui e adiciona na variavel
# arquivo.readlines le transformando em lista pulando linhas \n
# arquivo.readline() le somente uma linha
# arquivo.seek(0) zera a posicao do cursor (0)posicao de byte inicial
# 

######## EXEMPLO CRIAR E ALTERAR LISTA #########



while True:
    arquivox = input('Digite o nome do arquivo:')
    try:
        with open(arquivox, 'r') as arquivo:
            # arquivo.write('abacaxi \n')
            # print(arquivo.readline())
            # print(arquivo.readline())
            # arquivo.seek(0)
            # print(arquivo.readline())
            var = arquivo.readlines()
            break
    except Exception as error:
        print('Arquivo nao encontrado: {}'.format(error))
        

cont = 0
newlist = []

for x in var:
    x = x.replace('\n','-{}\n'.format(cont))# adiciona indice no fim 
    # newlist.append('{}-{}'.format(x, cont))
    newlist.append(x)
    cont += 1

with open ('new-frutas.txt','w+') as arquivo:
    for linha in newlist:
        arquivo.write(linha)

print(newlist)


exit()

############# EXEMPLO LEITURA E ESCRITA ##########
with open ('nomes.txt','a') as newname:
    while True:
        nome=input('Digite um nome ou (x) para sair : ')
        if nome.lower().strip() == 'x':
            break
        newname.write(nome + '\n')






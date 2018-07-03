#!/usr/bin///python3


def lerarquivo(nome_file):
    with open(nome_file, 'r') as arquivo:
        return arquivo.readlines()

def novalista(lista_parametro):
    try:
        cont = 0
        lista2 =[]
        # Tratamento da lista enumerando conteudo
        for x in lista_parametro:
            x = x.replace('\n','-{}\n'.format(cont))
            lista2.append(x)
            cont += 1
        # Escrevendo nova lista
        with open ('new-frutas-def.txt','w+') as arquivo:
            arquivo.write('#### NOVA LISTA #####\n')
            # for linha in lista2:
            #     arquivo.write(linha)
            arquivo.writelines(lista2)# escreve a lista sem FOR utilizando lista como variavel!
        return lista2
    except Exception as e:
        return "ERRO:{}".format(e)
        




arquivox = input('Digite o nome do arquivo: ') 

newlist= lerarquivo(arquivox)# Le o file e armazena na variavel newlist
listax = novalista(newlist)# cria nova lista

print('''
########################
# Nova lista reescrita #
########################
''')
print(listax)







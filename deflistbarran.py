#!/usr/bin/python3




# funcao altera lista

def lerlist(listax):
    newlist=[]
    for x in listax:
        # x = x.replace(x,x+'\n')# add \n com replace
        newlist.append('{}\n'.format(x))# add \n
    return newlist

def escr_list(parametro):
    try:
        with open('listanovabarran.txt','w') as arquivo:
            arquivo.writelines(parametro)
    except Exception as e:
        return 'Erro: {}'.format(e)


lista = ['fabio','mariaa','joao','carla','joana','ze','ana','shdasdhiasu']

# mostra  lista antiga
print (lista)
# mostra nova lista
print(lerlist(lista))

# chama funcao escreve nova lista
escr_list(lerlist(lista))


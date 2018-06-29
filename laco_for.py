#!/usr/bin/python3
nomes = ['fabio','carla','maria','joseee']
nomes2 = []
numeros = list(range(40,100))

# for nome in nomes:
#     print(nome.title())
#     nomes2.append(nome.title())
# print(nomes2)



#  for x in numeros: #contagem utilizando lista
#      print(x)

#  for x in range(40,100): # contagem em range
#     print(x, end="\n\n") # pula duas linhas
# exit()

#  for x in range(40,100,2):#contagem em passo 2
#     print(x)

#  for x in range(40,100,-2):#contagem decrescente
#     print(x)


num = int(input('Digite um numero: '))

for x in range(num):
    if x % 2 == 0:
        print('{} par'.format(x))
    else:
        print('{} impar'.format(x))


########### list string com for ############
# for x in range(97, 97 + 27):
#     print(chr(x))



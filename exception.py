#!/usr/bin/python3

from datetime import datetime

users = ['fabio','maria','jose','pedro']

while True:
    
    try:
        d = datetime.now()
        num = input('''

        Digite um usuario ou s para sair: 
        0 - fabio
        1 - maria
        2 - jose
        3 - pedro
        
        ''')
        if num.lower() == 's':
            break
        print('{} esta logado'.format(users[int(num)],))

    except IndexError as e:
        with open ('logPY.txt','a') as arquivo:
            result = 'Codigo de erro: {} , {} \n'.format(e,d.strftime('%Y-%m-%d %H:%M')) # .strftime('%Y-%m-%d %H:%M') formatacao de tempo
            arquivo.write(result)
        print('Usuario nao existe')
        break

    except KeyboardInterrupt as e: # para com ctrl-C
        with open ('logPY.txt','a') as arquivo:
            result = 'Codigo de erro: {} , {} \n'.format(e,d.strftime('%Y-%m-%d %H:%M')) # .strftime('%Y-%m-%d %H:%M') formatacao de tempo
            arquivo.write(result)
        print('Digitou CTRL-C')
        break

        









exit()
######### Ex Tratamento de erros #############
while True:
    try:
        num = int(input('digite um numero: '))
        print(num)
        break

    except ValueError as e: # Erro de valor
        print('nao é um inteiro: {}'.format(e))

    except Exception as e: # Exception todos os tipos de erro
        print('nao é um inteiro: {}'.format(e))
#!/usr/bin/python3

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
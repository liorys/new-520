#!/usr/bin/python3
from subprocess import subprocess

name = input("digite o nome do arquivo")
try:
    with open(name, 'r') as arquivo:
        conteudo = arquivo.readlines()
        conteudo.insert(0, '#!/usr/bin/python3\n')
    with open(name, 'w+') as arquivo:
        for x in conteudo:
            arquivo.write(x)

except FileNotFoundError:
    with open(name, 'a') as arquivo:
        arquivo.write('#!/usr/bin/python3\n')

run(['sudo', 'chmod', '+x', name])
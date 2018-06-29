#!/usr/bin/python3
nome = str(input('Digite o nome do aluno: \n'))
nota1 = float(input('Digite a primeira nota: \n'))
nota2 = float(input('Digite a segunda nota: \n'))
# nome = nome.title()
# nome = nome.replace("a","@")
# nome = nome.upper()
# nome = nome.lower()
media = (nota1 + nota2) / 2

if media >= 7:
    result = 'aprovado' #print('O aluno esta aprovado')
else:
    result = 'reprovado' # print('O aluno foi reprovado')

print('A media do aluno {} é de {} e esta {}'.format(nome.title().strip(),media,result))
print(nome)
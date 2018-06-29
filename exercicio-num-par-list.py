#!/usr/bin/python3

num = int(input('Digite um numero: \n'))
impar = []
par = []
if num % 2 == 1:
    print('o numero é impar adicionado no list impar')
    impar.append(num)
else:
    print('o numero é par adicionado no list par')
    par.append(num)

print('lista impar',impar)
print('lista par',par)


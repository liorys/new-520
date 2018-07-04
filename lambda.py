#!/usr/bin/python3
from random import randint,choice

anonimas = [lambda x: x**2,
            lambda x: x**3,
            lambda x: x**4,
            lambda x: x**5]
cont = 0
for a in anonimas:
    print(a(10))

exit()

for a in range(1,100):
    time.sleep(0.5)
    print(a)



'''
fruta = {'nome':'pera','preco':2.0,'qtd':10}
var = lambda x,y: x*y
times2 = lambda x:x*2

a = randint(0,10)
print(times2(a)

print(var(fruta['qtd'],fruta['preco']))
'''
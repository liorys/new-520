#!/usr/bin/python3
from random import choice,randint

nomess = ['fabio','maria','joao','carla']
'''
a = randint(0,1000)
print(choice(nomess),a)
'''

def random_choice(*args):
    return choice(args)


listax = []
with open ('nomes.txt','r') as arquivo:
    return(listax = arquivo.readlines())
    

print(choice(listax))

# print('Winner!',random_choice('fabio','maria','joao','carla'))
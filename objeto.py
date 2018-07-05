#!/usr/bin/python3

import time
class Car():
    def __init__(self,marca,modelo,ano,cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0
        self.combustivel = 'gasolina'


    def acelerar(self):
        self.velocidade += 10
        print('Acelerando...Velocidade:[{}]'.format(self.velocidade))

    def freiar(self):
        self.velocidade -= 10
        print('Freiando...Velocidade:[{}]'.format(self.velocidade))

    def parar(self):
        print('parado...')

class Car_eletric(Car):
    def __init__(self):
        self.combustivel = 'energia'


carro1 = Car('ford','ka',91,'verde')

car1 = Car_eletric()
car1.ano = 2002
car1.modelo ='BMW'



# print(carro1.anda())

while True:
    time.sleep(0.1)
    carro1.acelerar()
    if carro1.velocidade == 200:
        for x in range(carro1.velocidade):
            carro1.freiar()
            time.sleep(0.2)
            if carro1.velocidade == 0:
                carro1.parar()
                break
                    




exit()

######## OOP #######
class Dog():
    def __init__(self, nome, idade):# definir atributos da classe
        self.nome = nome
        self.idade = idade
        self.energia = 10

    def latir(self):# comportamentos
        print('Au au!')

    def andar(self):
        self.energia -= 1
        # if self.energia == 0:
        #     print('Estou cansado')
        print('andando...{}'.format(self.energia))

    def dormir(self):
        self.energia = 10
        print('dormindo....{}\n'.format(self.energia))



dog1 = Dog('haush',2)
dog2 = Dog('Pele',4)


print(dog2.nome)
print(dog1.nome)
dog1.latir()

while True:
    dog1.andar()
    time.sleep(0.2)
    if dog1.energia == 0:
        print('\nEstou cansado\n')
        dog1.dormir()





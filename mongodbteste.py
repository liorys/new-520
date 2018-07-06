#!/usr/bin/python3

from pymongo import MongoClient

try:
    client = MongoClient()
    db =  client['4linux']
except Exception as e:
    print('Erro:{}'.format(e))


######### Exemplo criacao de tabela ##########

frutas = [

    {'_id':1,'nome':'laranja','preco':2.0,'qtd':10},
    {'_id':2,'nome':'banana','preco':2.0,'qtd':20},
    {'_id':3,'nome':'maca','preco':2.0,'qtd':30},
]

# for x in frutas:
#     db.frutas.insert(x)

tabelafrutas = db.frutas.find()
tabelafrutas = [x for x in tabelafrutas]


for x in tabelafrutas:
    db.frutas.update(frutas(x))



print(type(tabelafrutas))


exit()

# Atualiza informacoes dentro do banco
db.pessoas.update({'_id':1},{'$set':{'nome':'Fabio','idade':27,'sobrenome':'Fugiyama'}})
# db.pessoas.remove({'_id':5})# remove a informacao do banco
# db.pessoas.insert({'_id':5,'nome':'blabla'})# adiciona no banco
# dados = db.pessoas.find_one({'_id':2})# busca informacoes na tabela com o ID passado
dados = db.pessoas.find()
dados = [x for x in dados]# List compression, tras as informaçoes em lista
print(dados)



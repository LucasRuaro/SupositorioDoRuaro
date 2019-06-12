import datetime
import peewee, os
from peewee import *

db = MySQLDatabase('sys', user='root', password='root')

class BaseModel(Model):

	class Meta:
		database = db

class Produto(BaseModel):
	nome = CharField()
	#Preço unitário ou por quilo
	preco = FloatField()

class Carrinho(BaseModel):
	tempo = DateTimeField(default=datetime.datetime.now)

class ItensCarrinho(BaseModel):
	#qtd pode ser em quilo ou unitário
	qtd_item = CharField()
	produtos = ForeignKeyField(Produto)
	carrinho = ForeignKeyField(Carrinho)

if __name__ == '__main__':
	try:
		db.connect()	
		db.create_tables([Produto, Carrinho, ItensCarrinho], safe=True)
		tabelas = [ItensCarrinho, Carrinho, Produto]
		for i in tabelas:
			d = i.delete()
			d.execute()

	except OperationalError as e:
		print("erro ao criar tabelas: "+str(e))

	produtos = {}
	nome_produtos = {
		'Naftalina': 100, 
		'Chocolate': 5
	}
	for nome, preco in nome_produtos.items():
		produtos[nome] = Produto.create(nome = nome, preco = preco)

	print(produtos)	
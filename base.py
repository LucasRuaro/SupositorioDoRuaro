import peewee, os
from peewee import *

db = MySQLDatabase('teste', user='root', password='root')

class BaseModel(Model):

    class Meta:
        database = db

class Produto(BaseModel):
    nome = CharField()
    #Preço unitário ou por quilo
    preco = FloatField()

class Carrinho(BaseModel):
    tempo = DateTimeField()

class ItemCarrinho(BaseModel):
    #qtd pode ser em quilo ou unitário
    qtd_item = CharField()
    produto = ForeignKeyField(Produto)
    carrinho = ForeignKeyField(Carrinho)

if __name__ == '__main__':
    try:
        db.connect()
        db.create_tables([Produto, Carrinho, ItemCarrinho], safe=True)
        q = ItemCarrinho.delete()
        q.execute()
        q = Carrinho.delete()
        q.execute()
        q = Produto.delete()
        q.execute()
    except OperationalError as e:
        print("erro ao criar tabelas: "+str(e))

    """print("TESTE DO ANIMAL")
    cli1 = Cliente(nome_cliente="José", cpf="15486354287")
    ani1 = Animal(nome_pet="Zed", tipo_animal="Dog", raca="Chiuaua", cliente=cli1)
    print(ani1)
    print("TESTE DA CONSULTA")
    con1 = Consulta(data="19/09/2018", servico="Consulta de rotina", 
    horario="14:00", animal=ani1, confirma="N", myID="c9d8f7gu4h3hnwsik3e")
    print(con1)
    print("TESTE DA PERSISTÊNCIA")
    cli1.save()
    ani1.save()
    con1.save()
    con2 = Consulta(data="21/09/2018", servico="Aplicação de vacina", 
    horario="10:00", animal=ani1, confirma="S", myID="d9firtu3434uit")
    con2.save()
    todos = Consulta.select()
    for con in todos:
        print(con)"""
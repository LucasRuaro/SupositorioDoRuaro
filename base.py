import peewee, os

db = peewee.MySQLDatabase('sys', user='root', password='root')

class Cliente(peewee.Model):
    nome_cliente = peewee.CharField()
    cpf = peewee.CharField()

    class Meta:
        database = db

    def __str__(self):
        return self.nome_cliente + ", cpf:" + self.cpf

class Animal(peewee.Model):
    nome_pet = peewee.CharField()
    tipo_animal = peewee.CharField()
    raca = peewee.CharField()
    cliente = peewee.ForeignKeyField(Cliente)

    class Meta:
        database = db

    def __str__(self):
        return self.nome_pet + ", " + self.tipo_animal + ", " + self.raca + " de " +str(self.cliente)

class Consulta(peewee.Model):
    data = peewee.CharField()
    servico = peewee.CharField()
    horario = peewee.CharField()
    animal = peewee.ForeignKeyField(Animal)
    confirma = peewee.CharField()
    myID = peewee.CharField()

    class Meta:
        database = db

    def __str__(self):
        return self.servico+" em "+self.data+":"+self.horario+", confirmado: "+\
        self.confirma+", ID da consulta: "+self.myID+" | animal: "+str(self.animal)

if __name__ == '__main__':
    try:
        db.connect()
        db.create_tables([Cliente,Animal,Consulta], safe=True)
        q = Consulta.delete()
        q.execute()
        q = Animal.delete()
        q.execute()
        q = Cliente.delete()
        q.execute()
    except peewee.OperationalError as e:
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
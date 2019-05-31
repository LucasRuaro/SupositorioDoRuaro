import peewee, os

db = peewee.SqliteDatabase('animalia.db')

class Cliente(peewee.Model):
	nome_cliente = peewee.CharField()
	cpf = peewee.CharField()

	class Meta:
		database = db
			
	def __str__(self):
		return self.nome_cliente + "," + self.cpf

class Animal(peewee.Model):
    nome_pet = peewee.CharField()
    tipo_animal = peewee.CharField()
    raca = peewee.CharField()
    cliente = peewee.ForeignKeyField(Cliente)

    class Meta:
        database = db

    def __str__(self):
        return self.nome_pet + "," + self.tipo_animal + "," + self.raca + " de " +str(self.cliente)

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
    arq = 'animalia.db'
    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Animal,Consulta]) 
    except peewee.OperationalError as e:
        print("erro ao criar tabelas: "+str(e))

    print("TESTE DO ANIMAL")
    a1 = Animal(nome_cliente="José", cpf="15486354287", tipo_animal="Dog", raca="Chiuaua")
    print(a1)

    print("TESTE DA CONSULTA")
    c1 = Consulta(data="19/09/2018", servico="Consulta de rotina", 
    horario="14:00", animal=a1, confirma="N", myID="c9d8f7gu4h3hnwsik3e")
    print(c1)

    print("TESTE DA PERSISTÊNCIA")
    a1.save()
    c1.save()
    c2 = Consulta(data="21/09/2018", servico="Aplicação de vacina", 
    horario="10:00", animal=a1, confirma="S", myID="d9firtu3434uit")
    c2.save()
    todos = Consulta.select()
    for con in todos:
        print(con)    
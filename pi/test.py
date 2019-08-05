import os
import serial 
from peewee import *
import datetime

arquivo = "arduino.db"
db=SqliteDatabase(arquivo)

class BaseModel(Model):

	class Meta:
		database=db

class TagPessoa(BaseModel):
	nome=CharField()
	nivel = CharField()
	tag_id=CharField(primary_key=True)

class Sala(BaseModel):
	pass
if __name__=="__main__":

	loop = 1

	if os.path.exists(arquivo):
		os.remove(arquivo)

	print("Criando tabelas...")
	db.connect()
	db.create_tables([TagPessoa])
	TagPessoa.create(nome="Rodacki Lindo", nivel="Professor", tag_id="1713d32b")
	TagPessoa.create(nome="Kalebe Gato", nivel="Aluno", tag_id="79e75559")

	try:
		print("Conectando com arduino...")
		port = 'COM4'
		arduino=serial.Serial(port)
		print("Arduino detectado")

		while loop > 0:

			bytes_recebidos = arduino.readline()
			print()
			print("Verificando tag...")
			tag_id = bytes_recebidos.decode("utf-8").rstrip() #converte os bytes em string
			tags = TagPessoa.select()
			for tag in tags:
				if tag.tag_id == tag_id:
					print("Acesso liberado!")
					print("Usuário:", tag.nome)
					print("Nível de acesos:", tag.nivel)
					break

				else:
					print("Tag não cadastrada:", tag_id)

			print()
			sair = input("Deseja sair? s/n: ")
			if sair == "s":
				break
			else:
				loop = 1
	except:
		print("Falha na conexão", port)

class Cliente():

    def __init(self,nome,email,telefone,senha):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha
    
class Animal():
    
    def __init__(self,nome,especie,aniversario):
        self.nome = nome
        self.especie = especie
        self.aniversario = aniversario

class Produto():
    def __init__(self,cod_produto,valor,quantidade):
        self.cod_produto = cod_produto
        self.valor = valor
        self.quantidade = quantidade

class Consulta():
    
    def __init__(self,cliente,animal,produto):
        super().__init__()



class ClienteCadastrado(Cliente):

    def __init(self,nome,email,telefone,senha):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha

class ClienteNaoCadastrado(Cliente):

    def __init(self,nome,email,telefone,senha):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha
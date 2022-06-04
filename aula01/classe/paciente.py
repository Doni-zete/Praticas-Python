""" 
classe - Um conjunto de objetos com as memsa caracteristicas
objeto -  Representação do mundo real como um tipo de dado de uma classe
construtor - É uma função criada  implitamente com o mesmo nome da classe
Atributo - São as variaveis de uma classe 
"""


class Paciente:

    def __init__(self, nome, idade, cpf, email):
        print("ok")
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email

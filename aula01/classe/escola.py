from abc import ABC, abstractclassmethod

# Classes Abstrata
class Pessoa(ABC):
  # superclasse - classe mãe, clase pai

    def __init__(self, nome=None, data=None, cpf=None, rg=None):
        self.nome = nome
        self.data_nascimento = data
        self.cpf = cpf
        self.rg = rg
        print("Executando o Construtor da classe")

    def imprimir_nome(self):
        return self.nome

    @abstractclassmethod
    def trabalhar(self):
        pass
# Classes Concretas
class Administrador(Pessoa):

    def trabalhar(self):
        nome_classe = self.__class__.__name__
        print(f"Classe {nome_classe} Organizando Planilhas...")

# Classes Concretas
class Professor(Pessoa):

    def __init__(self, nome):
        super().__init__(nome)
        self.disciplinas = []

    def trabalhar(self):
        nome_classe = self.__class__.__name__
        print(f"Classe {nome_classe} Ensinando...")

# Classes Concretas
class Aluno():
    # subclasse - classe filha, classe filho

    def __init__(self, nome):
        super().__init__(nome)
        self.matricula = None
        self.notas = []
        print("Classe aluno")

    def estudar(self):
        return "Estudando..."


professor1 = Professor('marcos')
Administrador1 = Administrador()
professor1.trabalhar()
Administrador1.trabalhar()




""" aluno1 = Aluno('ana')
print(aluno1.imprimir_nome())


professor1 = Professor("MArcos")
print(professor1.imprimir_nome())

print(aluno1.estudar())
print(professor1.lecionar()) """

""" print(type(aluno1))
print(type(professor1))


  """


# get e set

""" # get e set
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade

aluno1 = Aluno('Jose', 15, 123456)

print(aluno1.nome)
aluno1.nome = 'josep'
print(aluno1.nome)


print(aluno1.idade)
aluno1.idade = 23
print(aluno1.idade)

 """


# class Quadrado


""" class Quadrado:

  def __init__(self, lado):
      self.__lado = lado
      self.__area = lado * lado

  def retorna_area(self):
      print(self.__area)   

quadrado = Quadrado(2)         
quadrado.retorna_area()  
quadrado.area = 7
quadrado.retorna_area()
print(quadrado.__dict__)
quadrado._Quadrado__area = 13
quadrado.retorna_area()  
 """

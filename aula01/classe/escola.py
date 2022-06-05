class Aluno:

    def __init__(self, nome, idade, matricula):
        self.__nome = nome
        self.idade = idade
        self.matricula = matricula
        self.notas = None

# get e set
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

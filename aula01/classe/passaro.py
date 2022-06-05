class Passaro:
    def __init__(self, sons, voar, nome_classe):
        self.sons = sons
        self.voar = voar
        self.nome_classe = nome_classe
      
    def voando(self):
        print(self.nome_classe, "voa e faz", end= ' ')

class Pato(Passaro):
    def __init__(self, sons, voar):
        super().__init__(sons, voar, self.__class__.__name__)

    def som(self):
        print("quack quack", end = ' ')

class Galinha(Passaro):
    def __init__(self, sons, voar):
        super().__init__(sons, voar, self.__class__.__name__)

    def som(self):
        print("có có có", end = ' ')


class Pardal(Passaro):
    def __init__(self, sons, voar):
        super().__init__(sons, voar, self.__class__.__name__)

    def som(self):
        print("piu piu", end = ' ')


pato1 = Pato('pato', 'voar')
pato1.voando()
pato1.som()


pardal1 = Pardal('pardal', 'voar')
pardal1.voando()
pardal1.som()

gainha = Galinha('galinha', 'bica')
gainha.voando()
gainha.som()




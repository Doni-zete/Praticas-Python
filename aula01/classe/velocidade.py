class Carro():

    def __init__(self, v_inicial=5):
        self.__velocidade = v_inicial

    def aumentaVelocidade(self):
        self.__velocidade = self.__velocidade + 2

    def setVelocidade(self, novaVelocidade):
        if novaVelocidade >= 0:
            self.__velocidade = novaVelocidade

    def getVelocidade(self):
        return self.__velocidade


carro1 = Carro()
carro1.setVelocidade(10)
print(f'velocidade atual:  {carro1.getVelocidade()}')
# carro1.__velocidade = 50
# carro1.__velocidade = carro1.__velocidade * -1
# print(carro1.__velocidade)

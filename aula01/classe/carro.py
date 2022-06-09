from veiculo import Veiculo


class Carro (Veiculo):
    def __init__(self, tipo, modelo, km, portas):
        Veiculo.__init__(self, tipo, modelo, km)
        self.portas = portas

    def exibe(self):
        print(self.tipo, "modelo", self.modelo, "com", self.km,
              "km rodados e", self.portas, "portas.")

    # def liga(self):
    #     print("Liga meu carro")          


palio = Carro("Carro", "Palio", "10000", 2)
palio.liga ("gol")
# palio = Carro.ligae("gol", 2011)
palio.exibe()
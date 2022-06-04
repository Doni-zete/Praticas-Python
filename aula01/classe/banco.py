"""
Visibilidade -  Modificador de Acesso
privada (private) - restritiva -> Define que os atributos  e métodos só podem seer manipulados dentro da clase.
protegida (protected) - intermediaria -> Define que os atributos e metodo só podem ser manipulados dentro da classe e nas classes que herdam da classe ondem froma definidos.
publica(public) - menos restritiva -> Define que os atributos emétodos são acessiveis em queal quer lugar.
"""

class Conta:

    # Atributo de Classe
    taxa = 0.50

    @classmethod
    def retornarCodigo(self):
        print("Codigo: 555")

    @staticmethod
    def retornarCodigoBanco():
        return '345'

    # Atributos de Instâncias
    def __init__(self, numero, titular, saldo=2000):
        self._numero = numero  # Visibilidade protegida(protected)
        self.titular = titular # Visibilidade publica(public)
        self.__saldo = saldo # Visibilidade privada(private)

    def extrato(self):
        print(f'Saldo: R${self.__saldo}')

    def depositar(self, valor):
        self.__saldo += valor
        print('Deposito realizado com sucesso')

    def sacar(self, valor):
        self.__saldo -= valor
        print('Saque realizado com sucesso')

# Instancias da Classe Conta


conta1 = Conta(123, 'Joao Carlos', 10000)
conta2 = Conta(1234, 'Maria joana')

""" print(f'Titular: {conta1.titular} - Saldo: R${conta1.__saldo}')
print(f'Titular: {conta2.titular} - Saldo: R${conta2.__saldo}') """

""" print(conta1. __dict__)
print(conta2. __dict__)

conta2.extrato()
conta1.extrato()

# Atributo Dinâmico -> Criado em tempo de execução
conta2.signo = 'Peixes'

print(conta1. __dict__)
print(conta2. __dict__)

del conta2.signo
print(conta1. __dict__)
print(conta2. __dict__)

# Metodo da classe
Conta.retornarCodigo()  # Convenção
conta1.retornarCodigo()

# Método Estático
print(Conta.retornarCodigoBanco())  # Convenção
print(conta2.retornarCodigoBanco())
 """
from datetime import date


class Paciente:

    def __init__(self, nome, idade, cpf, email):
        print("Acessei o construtor")
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email

    @classmethod
    def idadeAnoNascimento(self, nome, anoNascimento, cpf, email):
        idade = date.today().year - anoNascimento
        return self(nome, idade, cpf, email)


class Medico:
    pass


""" 
paciente = Paciente('Mona Lisa', 20, '000.000.000-00', 'mona@gmail.com')
print(paciente.__dict__)
print(Paciente.idadeAnoNascimento(2001)) """

paciente = Paciente.idadeAnoNascimento('Mona Lisa', 1957, '000.000.000-00', 'mona@gmail.com')
print(paciente.__dict__)
print(paciente.idade)
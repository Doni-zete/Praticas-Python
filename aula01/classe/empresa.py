class FunciAonario:
    def trabalhar(self):
        print("Trabalhando")


class FronEnd(Funcionario):
    def fron_end(self):
        super().trabalhar()


class BacKEnd(Funcionario):
    def back_end(self):
        super().trabalhar()


class FullStack(FronEnd, BacKEnd):
    pass


ana = FullStack()
ana.back_end()
ana.fron_end()

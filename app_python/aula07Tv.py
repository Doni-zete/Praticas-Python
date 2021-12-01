class Televisao:
    def __init__(self):
        self.ligada =False
        self.canal =5

    def power(self):
            if self.ligada:
                self.ligada= False
            else:
                self.ligada =True

    def aumenta_Canal(self):
             self.canal+=1
    def diminui_canal(self):
            self.canal-=1


televisao = Televisao()
print('Televisao esta ligada:{}'.format(televisao.ligada))
televisao.power()
print('Televisao esta ligada:{}'.format(televisao.ligada))
televisao.power()
print('Televisao esta ligada:{}'.format(televisao.ligada))
print('Cnal: {}'.format(televisao.canal))
televisao.aumenta_Canal()
televisao.aumenta_Canal()
print('Canal: {}'.format(televisao.canal))
televisao.diminui_canal()
print('Canal: {}'.format(televisao.canal))

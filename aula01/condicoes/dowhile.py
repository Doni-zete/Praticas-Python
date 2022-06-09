""" 
do while
Codigo para adivinhar um numero
 """

palpite = 0
numero = 9

# while palpite != numero:

while True:
    print("Qual o numero correto? ")
    palpite = int(input())
    if palpite == numero: #Estamos verificaando nosso código
        print("Parabens voce acertou")
        break
    else:
        print("Voce errou")
else:
    print("Erro na aplicção")
    print(bool(palpite))

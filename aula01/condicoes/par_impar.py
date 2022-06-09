"""
Decobrir se um numero é impar oou par
"""

print(25*"-")
while True:
    numero = int(input("Digite um numero: "))

    if (numero % 2) == 0:
        print(f"Numero digitado, {numero} é PAR: ")
    elif(numero % 2) != 0:
        print(f"Numero digitado, {numero} é IMPAR: ")
    print(25*"-")

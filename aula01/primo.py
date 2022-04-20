
"""
Descobrir se um numero e primo
"""

numero = int(input("Digite um numero: "))
if numero > 1:
    for x in range(2, numero):
        if(numero % x) == 0:
            print("Esse não e um numero primo")
            break
    else:
        print("Esse numero e um numero primo")
else:
    print("Esse numero não e primo: numero menor ou igual a 1")

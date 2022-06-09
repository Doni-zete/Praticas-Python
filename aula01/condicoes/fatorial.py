
"""
Como achar o fatorial de um número
"""
numero = int(input("Insira um numero:"))
fatorial = 1

if numero < 0:
    print("Não existe fatorial de numeros negativos")
elif numero == 0:
    print(f"O fatorial de {numero} eh 1")
else:
    for x in range(1, numero+1):
        fatorial = fatorial*x
        print(f"o fatorial de {numero} eh: {fatorial}")

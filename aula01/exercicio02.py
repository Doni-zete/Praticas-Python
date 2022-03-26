""" idade = input('Entre com sua idade: ')

if int(idade) < 16:
    print('MENOR')
elif int(idade) >= 16 & int(idade) <= 18:
    print('EMANCIPADO')
elif int(idade) > 18:
    print('MAIOR') """


""" a = 8
b = 3
c = 1 """
""" if a > b: print("b eh maior do que a")
print("Codigo fora do bloco if") """

# print("B") if b < a else print("A") # Operador ternario

""" if a > b:
    print("A")
    if a > c:
        print("A eh maior que b e que c") """

a = input("Entre com sua idade:")
idade = int(a)

if idade <= 7:
    print("Infantil A")
elif idade <= 10:
    print("Infantil B")
elif idade <= 13:
    print("Juvenil A")
elif idade <= 17:
    print("juvenil B")

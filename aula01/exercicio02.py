""" idade = input('Entre com sua idade: ')

if int(idade) < 16:
    print('MENOR')
elif int(idade) >= 16 & int(idade) <= 18:
    print('EMANCIPADO')
elif int(idade) > 18:
    print('MAIOR') """


a = 8
b = 3
c = 1
""" if a > b: print("b eh maior do que a")
print("Codigo fora do bloco if") """

# print("B") if b < a else print("A") # Operador ternario

if a > b:
    print("A")
    if a > c:
        print("A eh maior que b e que c")

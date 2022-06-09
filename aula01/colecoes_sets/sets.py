""" sets: Coleção não ordenada, imutavel e que não permite valores duplicados"""

# Definir sets
conjunto = {"item1", "item2", "item3", "item2", "item3"}
print(type(conjunto))
print(conjunto)
print(len(conjunto))

tupla = (3, 7, 7, 9, 5, 5)
conjunto = set(tupla)
print(conjunto)

conjunto = {3, 7, 9, 5}

conj = {"item1", "item2", "item3"}

for x in conj:
    print(x)
    conjunto = {3, 7, 9, 5}
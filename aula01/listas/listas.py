""" lista = ["chicago", "queens", "Ronaldo", "Listao"]
print(lista)

lista2 = [52, 2, 6, 9, 200]
print(lista2)

lista3 = [True, False]
print(lista3)
# index     0       1        2     3     5
lista5 = [True, "chicago", 2.5, False, 4, 8]
print(lista5)

print(type(lista3))
print(lista5[4])

print(lista5[-1])
# :: chama todos elementos
print(lista5[::])
print(lista5[1:4])
print(lista5[1:4:2])

nome5 = "terra"

print(nome5[2:4])

lista = lista2 + lista3
print(lista2)
 """

lista1 = [2.0, 3.5, 4.7]
print(lista1)
lista2 = [1, 5, 9, 11, 15]
print(lista2)
# Tamanho da lista -função len
print(len(lista1))
print(len(lista2))
# Função que só podem ser utilizadas com tipos de dados numericos


print(sum(lista1))  # somatorio dos elementos da nossa lista
x = 2.0 + 3.5 + 4.7
print(x)

print(max(lista2))  # Retorna o elemento de valor máximo da lista
print(min(lista2))  # Retorna o elemento de valor minimo da lista

nome = "Curso de Python"
valor = range(10)

print(nome)
print(valor)

lista7 = list(range(10))
print(lista7)


lista8 = list("Curso de Python")
print(lista8)

elemento = 8
if elemento in lista7:
    print("Este elemento esta dentro da lista")

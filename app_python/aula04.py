lista =[12,10,5,7]
lista_animal =['cachorro,','gato','elefante','lobo,','arara']

lista_animal[0]='macaco'
print(lista_animal)

tupla =(1,10,12,14)
print(len(tupla))
print(tupla[3])
tupla_animal =tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica =list(tupla)
print(type(lista_numerica))
lista_numerica[0]=100
print(lista_numerica)


# print(lista_animal[1])
# novo_lista = lista_animal *3
# print(novo_lista)

# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal)




# if 'lobo' in lista_animal:
#     print('existe um gato na lista')
# else:
#     print('não existe um lobo na lista. Sera incluido')
#     lista_animal.append('lobo')
#     print(lista_animal)


    # lista_animal.remove('elefante')
    # print(lista_animal)


    # lista_animal.pop(1)
    # print(lista_animal)

# print(sum(lista))
# print(max(lista))
# print(min(lista_animal))
# soma=0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)
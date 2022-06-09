lista = []


def entradaUserCrip():
    return input("Digige sua frase: ")


def entradaUserDesc():
    return input("Digige seu codigo para descriptografar: ")


def equivalenteUnicode(str):
    for frase in str:
        lista.append(ord(frase))
    return lista


def retornaInteiro(listas):
    for char in listas:
        ascii = ord(char)
        print(char + str(ascii))


print("O codigo Criptografado é: {0}".format
      (equivalenteUnicode(entradaUserCrip())))
print("O codigo descriptografado é ",
      chr(retornaInteiro(entradaUserDesc())))


""" def retornaInteiro(str):
    for numero in str:
        lista.append(chr(numero))
    return lista """

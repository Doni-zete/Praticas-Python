lista = []


def typeUser():
    return input()


def equivalenteUnicode(value):
    listcara = list(map(ord, value))
    return list(map(str, listcara))


def retornaCaractere(listas):
    return list(map(chr, listas))


# print("TESTANTO: {0}".format(equivalenteUnicode(typeUser())))


def spliText():
    textArray = input("Digite aqui : ").split(" ")
    textList = list(map(int, textArray))

    # print(textList)

    # print(retornaCaractere(textList))

    return textList


# spliText()
def initializeCode():
    condicao = int(input("(1) Digitar 'numero'\n(2) Digitar 'string'\n "))
    print("Opção escolhida: {} ".format(type(condicao)))

    result = ""

    if condicao == 1:
        result = "".join(retornaCaractere(spliText()))
    else:
        result = " ".join(equivalenteUnicode(input()))
    print(result)


initializeCode()

# def soma1(x):
#     return x + 1
# num1Array = [1, 1, 1, 4, 1, 1]
# # retornaInterio(map(ord, ['s', 'a', 'f', 'a', 'd', 'o']))

# print(list(map(soma1, num1Array)))


# print(list(map(ord, ['s', 'a', 'f', 'a', 'd', 'o'])))

# test = "Zete programador"
# print(list(map(ord, test)))
# test2 = list(map(ord, test))

# print(list(map(chr, test2)))

# print("".join(list(map(chr, test2))))

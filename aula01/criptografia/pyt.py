def equivalenteUnicode(str):
    return list(map(ord, str))


def retornaCaractere(listas):
    return list(map(chr, listas))


print(35*"=")


def spliText():
    textArray = input("Digite aqui: ").split(" ")
    textList = list(map(int, textArray))

    return textList


def initiacializarCodigo():
    condicao = int(
        input(" Digitar (1) Criptografar\n Digitar (2) Descriptografar\n "))
    print(30*"-")
    print("Opção escolhida: {} {} ".format(condicao, type(condicao)))

    result = ""

    if condicao == 1:
        result = "Tabela ASCII", equivalenteUnicode(input())

    else:
        result = retornaCaractere(spliText())

    print(result)


initiacializarCodigo()

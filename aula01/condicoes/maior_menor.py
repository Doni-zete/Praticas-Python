listanum = []
maior = 0
menor = 0
for numero in range(0, 5):
    listanum.append(int(input(f"Entre com um numero {numero}: ")))
    if numero == 0:
        maior = menor = listanum[numero]
    else:
        if listanum[numero] > maior:
            maior = listanum[numero]
        if listanum[numero] < menor:
            menor = listanum[numero]

    print("=-" * 30)
print(f"Voce digitou os valores {listanum}")
print(f"O maior valor digitado foi {maior} nas posiçoes ", end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f"{i}... ", end='')
print()
print(f"O menor valor foi {menor}  nas posiçoes ", end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f"{i}...", end='')

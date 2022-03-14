""""
nome = input("Qual e o seu nome?")
idade = input("Qual é sua idade? ")

print("Ok, seu nome e: {0} e Sua idade é: {1}".format(nome,idade))
"""

""" nome = input("Qual e o seu nome?")
idade = input("Qual é sua idade? ")
print(f'Ok, seu nome é: {nome} e sua idade:{idade}') """


# altura = input("Entre com a altura: ")
# largura = input("Entre com a base: ")

# area = float(altura) * float(largura)
# print(f'A area é: {area}')

valorProduto = input("Entre com o valor do produto: ")
valorDesconto = input("Entre com o desconto em porcentagem: ")

porcentagem = float(valorProduto)*(float(valorDesconto)/100)
conta = float(valorProduto)-float(porcentagem)
print(f'Valor com R${porcentagem} de desconto dá R$: {conta}')

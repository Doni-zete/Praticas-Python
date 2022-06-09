# Listas: Coleção ordenada, mutável e que permite valores duplicados
# Tuuplas: Coleção, imutavel e que permite valores duplicados
# Dicionarios: Coleção não ordenada, mutavel e que não permite valores duplicados

# index
lista = {"item2", "item3", "item2"}
tupla = {"item1", "item2", "item1"}

# chave:valor
dados = {"nome": "Gabriel", "ano": 1993, "valor_logico": True}
print(dados)

dicionario = {
    "nome": "Bruna",
    "idade": 27,
    "nacionalidade": "brasileira"
}

""" print(dicionario)
print(dicionario['idade'])
print(dicionario.get('idade'))
print(dicionario.keys())
print(len(dicionario))
print(dicionario.values())

if "idade" in dicionario:
  print("A chave idade exite")
else:
  print("não existe")

print(dicionario.items())  
 """

# modificar
dados['idade'] = 32
print(dados)

dados.update({"nome": "Ana"})
print(dados)


dados.update({"Estado": "Rio de janeiro"})
print(dados)

# A função popite, elimina o último item apenas da versão 3.7 e acima
dados.popitem()  # nas outras versões (abaixo da 3.7) essa função elimina um item aleatorio
print(dados)

dados.pop("valor_logico")
print(dados)

# deleta
""" del dados["ano"]
print(dados)

dados.clear()
print(dados) """

""" for x in dados.items():
    print(x)

dicio = dados.copy()
print(dicio)

dicio2 = dict(dados)
print(dicio2)

dados["idade"] = 27
print(dados)
print(dicio)
print(dicio2) """


""" tupla = ("item", "item2", "item3 ")
x = 0
dicio = dict.fromkeys(tupla, x)
print(dicio) """

dicio = {
    "dicio1": {
        "nome": "Ana",
        "idade": 25,
    },
    "dicio2": {
        "nome": 38,
        "dicio3": {
            "nome:": "ANa juli",
            "idade": 5
        }
    }
}

print(dicio)
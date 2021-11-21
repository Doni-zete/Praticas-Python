# a = int(input("Primeiro numero:"))
# b = int(input("Segundo numero:"))
# c = int(input("Terceiro numero:"))
# if a > b and a >c:
#     print("O maior numero e {}".format(a))
# elif b> a and b>c:
#     print("o maior numero e {}".format(b))
# else:
#     print("o maior numero e {}".format(c))
#     print ("final do programa")

# a= int (input("Entre com um valor: "))
# b= int (input("Entre com o segundo valor: "))
# resto_a = a%2
# resto_b = b%2
# if resto_a ==0 or not resto_b>0:
#     print("numero e par")
# else:
#     print(("nenhum numero par digitado "))
nota1 =int (input("Primeira nota: "))
if nota1>10:
    a= int(input("Voce digitou a primeira nota errada"))
nota2 =int(input("segunda nota: "))
if nota2>10:
    nota2= int(input("Voce digitou a segunda nota errada"))
nota3 =int(input("terceiro nota: "))
if nota3 >10:
    nota3 = int(input("Voce digitou a terceira nota errada"))
nota4 =int(input("quarto nota: "))
if nota4 >10:
    nota3 = int(input("Voce digitou a quarta nota errada"))
media= (nota1+nota2+nota3+nota4)/4
print("nota do aluno e " + str(media))
# if nota1<=10and nota2<=10and nota3<=10 and  nota4<=10:

# else:
#     print("Nota digitada errada")
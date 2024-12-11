# Escreva um programa que leia três números e seus respectivos pesos e calcule a sua
# média ponderada.

print("\nINFORME 3 NÚMEROS INTEIROS E SEUS RESPECTIVOS PESOS\n")

num1 = float(input("Digite o primeiro número: "))
peso1 = float(input("Digite o peso para o primeiro número: "))

num2 = float(input("Digite o segundo número: "))
peso2 = float(input("Digite o peso para o segundo número: "))

num3 = float(input("Digite o terceiro número: "))
peso3 = float(input("Digite o peso para o terceiro número: "))

media_ponderada = (num1*peso1 + num2*peso2 + num3*peso3)/ (peso1 + peso2 + peso3)

print(f"A média ponderada dos valores digitados é {media_ponderada:.3f}")

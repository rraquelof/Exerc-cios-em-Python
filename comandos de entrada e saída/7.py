# Escreva um programa que leia o valor da base e da altura de um triângulo e calcule
# a sua área.

base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))

area = (base * altura)/2

print(f"A área do triangulo é: {area:.3f}")
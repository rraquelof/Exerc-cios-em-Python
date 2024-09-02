# Escreva um programa que leia o valor do lado de um quadrado e calcule a sua área e o
# seu perímetro.

lado = float(input("Digite o valor do lado do quadrado: "))

area = lado **2
perimetro = lado * 4

print(f"A área do quadrado é {area:.2f}")
print(f"O perímetro do quadrado é {perimetro:.2f}")
# Escreva um programa que leia o valor do raio de uma circunferência e calcule a sua
# área e o seu comprimento.
from math import pi

valor_raio = float(input("Digite o valor do raio da circunferência: "))

area = pi * (valor_raio **2)
comprimento = 2 * pi * valor_raio

print(f"A área da circunfêrencia é {area:.3f}")
print(f"O comprimento da circunfêrencia é {comprimento:.3f}")
# Escreva um programa que leia um número inteiro positivo e calcule o seu dobro, o seu
# triplo, o seu quadrado, o seu cubo e a sua raiz quadrada.
from math import sqrt

num = int(input("Digite um número inteiro positivo: "))

while num < 0:
    print("Por favor, digite um número positivo\n")
    num = int(input("Digite um número inteiro positivo: "))
else:
    dobro = num * 2
    triplo = num * 3
    quadrado = num ** 2
    cubo = num ** 3
    raiz = sqrt(num)
    
    print(f"O dobro de {num} é: {dobro}")
    print(f"O triplo de {num} é: {triplo}")
    print(f"O quadrado {num} é: {quadrado}")
    print(f"O cubo {num} é: {cubo}")
    print(f"A raiz de {num} é: {raiz}")

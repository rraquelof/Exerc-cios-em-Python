# Escreva um programa que leia um número inteiro e verifique se ele é par ou ímpar.
def parOuImpar():
    try:
        numero = int(input("Digite um número: "))
        if numero % 2 == 0:
            print(f"O número {numero} é par!")
        else:
            print(f"O número {numero} é impar!")
    except ValueError:
        print("Inválido! digite um número inteiro.")

parOuImpar()
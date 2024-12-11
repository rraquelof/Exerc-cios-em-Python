# Escreva um programa que leia dois números e determine se o segundo número é
# menor, igual ou maior que o primeiro.

def compararNumeros():
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        if numero1>numero2:
            print(f"{numero1} é maior que {numero2}")
        elif numero2>numero1:
            print(f"{numero2} é maior que {numero1}")
        else:
            print(f"{numero1} e {numero2} são iguais.")
    except ValueError:
        print("Valor inválido!")

compararNumeros()
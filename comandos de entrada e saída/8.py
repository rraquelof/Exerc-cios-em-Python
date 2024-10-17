# Escreva um programa que leia o valor de uma temperatura em Celsius e calcule o seu
# valor correspondente em Fahrenheit e em Kelvin.

celsius = float(input("Digite a temperatura em graus celsius: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"Temperatura em Fahrenheit: {fahrenheit:.2f}°F")
print(f"Temperatura em Kelvin: {kelvin:.2f} K")
# Escreva um programa que leia a idade de uma pessoa e verifique se ela é criança (0-12
# anos), adolescente (13-17 anos), adulta (18-59) ou idosa (acima de 60 anos).

def verFaixaEtaria():
    try:
        idade = int(input("Digite sua idade: "))
        if 0 <= idade <= 12:
            print("Criança")
        elif 13 <= idade <= 17:
            print("Adolescente")
        elif 18 <= idade <= 59:
            print("Adulto")
        elif idade >= 60:
            print("Idoso")
        else:
            print("Idade inválida!")
    except ValueError:
        print("Valor inválido!")

verFaixaEtaria()
# Crie um programa que peça o nome, idade, peso e altura de uma pessoa. Com o peso e altura deve ser calculado o imc da pessoa. O resultado deve ser mostrado como perfil.

print("Seja bem vindo ! \n")

nome = input(" Qual seu nome? ")

idade = int(input(" Qual a sua idade? "))

peso = float(input("Qual seu peso? "))

altura = float(input("Qual a sua altura ? "))

imc = peso/(altura * altura)

print(f"Olá {nome}!")
print(f"Sua idade é de {idade} anos.")
print(f"Seu IMC é {imc: .2f}.")
             
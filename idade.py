#Crie um programa que peça ao usuário para inserir sua idade e, em
#seguida, informe se a pessoa é menor de idade ou maior de idade.

print("=======Verificação de Idade=======")
print("==================================")

idade = int(input("Informe sua idade?"))

if idade >= 18:
    print("Você é de maoir!")

else:
    print("Você ainda não é de maior!")

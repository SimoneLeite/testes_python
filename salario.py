#Peça ao usuário para inserir seu salário e o tempo de serviço. Se o tempo de serviço for superior a 5 anos, conceda um bônus de 5% ao salário.

print("=====CÁCULO DE ABONO SALARIAL=====")

# Solicita ao usuário que insira o salário e o tempo de serviço
salario = float(input("Digite o valor do seu salário: "))
tempo_de_servico = int(input("Digite o tempo de serviço (em anos): "))

# Verifica se o tempo de serviço é superior a 5 anos
if tempo_de_servico > 5:
    # Calcula o bônus de 5% no salário
    bonus = salario * 0.05
    salario += bonus  # Adiciona o bônus ao salário original

    # Exibe o novo salário com o bônus
    print(f"Parabéns! Você recebeu um bônus de 5% e seu novo salário é: R${salario:.2f}")
else:
    # Caso o tempo de serviço seja igual ou inferior a 5 anos
    print("Você não é elegível para receber um bônus neste momento.")



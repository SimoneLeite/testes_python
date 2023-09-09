# Programa para calcular taxa de juros

print("*******************************")
print("*******CALCULANDO JUROS********")
print("*******************************")

valor = float(input("Qual o valor que deseja calcular?"))

tempo = float(input("Qual o período de tempo?"))

juros = float(input("Informe a taxa de juros anual em porcentagem ?"))


montante = valor + (valor * (juros/100) * tempo)

print("RESULTADO")

print(f"O total do montante final é {montante}")
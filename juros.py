print("*******************************")
print("*******CALCULANDO JUROS********")
print("*******************************")

valor = float(input("Qual o valor que deseja calcular?"))

tempo = int(input("Qual o período de tempo?"))

juros = float(input("Informe a taxa de juros anual?"))

juros1 = juros/100


montante = valor + (valor * juros1 * tempo)

print("RESULTADO")

print(f"O total do montante final é {montante}")
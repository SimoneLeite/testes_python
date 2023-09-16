#Peça ao usuário para inserir dois números e uma operação (+, -, *, /).
#Realize a operação e exiba o resultado.

print("=======CALCULADORA SIMPLES=======")
print("=================================")

numero1 = float(input("Informe o primeiro número? "))
numero2 = float(input("Informe o segundo número? "))
operacao = input("Escolha umas das operaçoes (+, -, *, /)")

if operacao == "+":
    resultado = numero1 + numero2
    print(f"O resultado é : {resultado} ")
elif operacao == "-":
    resultado = numero1 - numero2
    print(f"O resultado da subtração é : {resultado}")
elif operacao == "*":
     resultado = numero1 * numero2
     print(f"O resultado da subtração é :{resultado}")
elif operacao == "/":
     if numero2 == 0:
          print("Não é possível dividir esse valor.")
     else:     
          resultado = numero1 / numero2
else :
     print("Opreação não reconhecida")

if resultado != '':
     print(f"O resultado é: {resultado}")

    
    



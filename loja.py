print("======LOJA DE ROUPAS======")
print("==========================")


valor_Compra = float(input(" Digite o valor da compra ? R$"))

pagamento = (input("Digite a forma de pagamento: à vista ou prazo ? "))

total = valor_Compra

parcelas = valor_Compra

if pagamento == "vista":
    if valor_Compra <= 500:
        total = valor_Compra * 0.9
        print(f"Valor da total da compra foi de : R$ { total }")
    elif valor_Compra > 500 and valor_Compra <= 1000: 
        total = valor_Compra * 0.85
        print(f"O valor total da compra é : R$ {total}")
    elif valor_Compra > 1000:
        total = valor_Compra * 0.8
        print(f"O valor total da sua compra foi de : R$ {total} ")  


if pagamento == "prazo":
    if valor_Compra <= 800:
        print(input(" Esse valor pode ser parcelado em até 4x sem juros ")) 
        parcelas = float(input("Digite a quantidade de parcelas:"))
        total = valor_Compra / parcelas 
        print(input(f"Vão ser {parcelas} x parcelas de {total:.2f}")) 

    if valor_Compra > 800:
        print(input("Esse valor pode ser dividido em até 18x, sendo que até 10 s/ juros.")) 
        parcelas = float(input("Digite a quantidade de parcelas:")) 
        if parcelas <= 10:
            total = valor_Compra / parcelas
            print(input(f"Vão ser {parcelas} x de {total:.2f}"))

        elif parcelas == 11:
            juros = 0.05
            total = valor_Compra + (valor_Compra * parcelas * juros)
            valor_mes = total / parcelas
            print(input(f"Vão ser {parcelas} parcelas de {valor_mes:.2f}"))

        elif parcelas == 12:
            juros = 0.065
            total = valor_Compra + (valor_Compra * parcelas * juros)
            valor_mes = total / parcelas
            print(input(f"Vão ser {parcelas} parcelas de {valor_mes:.2f}"))

        elif parcelas == 13:
            juros = 0.07
            total = valor_Compra + (valor_Compra * parcelas * juros)
            valor_mes = total / parcelas
            print(input(f"Vão ser {parcelas} parcelas de {valor_mes:.2f}"))
    

        elif parcelas == 14:
            juros = 0.09
            total = valor_Compra + (valor_Compra * parcelas * juros)
            valor_mes = total / parcelas
            print(input(f"Vão ser {parcelas} parcelas de {valor_mes:.2f}"))

        elif parcelas == 15:
            juros = 0.095
            total = valor_Compra + (valor_Compra * parcelas * juros)
            valor_mes = total / parcelas
            print(input(f"Vão ser {parcelas} parcelasde {valor_mes:.2f}"))
            
        elif parcelas == 16:
            juros = 0.1
            total = valor_Compra + (valor_Compra * parcelas * juros)
            valor_mes = total / parcelas 
            print(input(f"Vão ser {parcelas} x parcelas de {valor_mes:.2f}"))

        elif parcelas == 17:
            juros = 0.113
            total = valor_Compra + (valor_Compra * parcelas * juros) 
            valor_mes = total / parcelas
            print(input(f"Vão ser {parcelas} x parcelas de {valor_mes:.2f}"))

        elif parcelas == 18:
            juros = 0.12
            total = valor_Compra + (valor_Compra * parcelas * juros)
            valor_mes = total / parcelas
            print(input(f"Vão ser {parcelas} parcelas de {valor_mes:.2f}"))
        else:
            print("Número de parcelas inválido para esta forma de pagamento.")
    else:
        print("Forma de pagamento inválida. Por favor, escolha entre 'à vista' ou 'prazo'.")

        
    

        
    

    
    

    
    

    
    



             



   

   



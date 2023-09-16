#Peça ao usuário para inserir uma nota de 0 a 100 e, em seguida, classifique-a como
#"A" (90-100), "B" (80-89), "C" (70-79),
#"D" (60-69) ou "F" (abaixo de 60).

print("====Notas====")

nota = float(input("informe sua nota de 0 a 100: "))

classificao = ''

if nota >= 0 and nota <= 100:
    if  nota >= 90:
        classificao = "A" 
    elif nota >= 80 and  nota <= 89:
        classificao = "B" 
    elif nota >= 70 and nota <= 79 :
        classificao = "C"
    elif nota >= 60 and nota <= 69 :
        classificao = "D"  
    else:
        classificao = "F"
    print(f"Classificação da nota: {classificao}")     
else :
    print("Nota fora do parãmetro pedido ( de 0 a 100)")


     


#Peça ao usuário para inserir uma nota de 0 a 100 e, em seguida, classifique-a como
#"A" (90-100), "B" (80-89), "C" (70-79),
#"D" (60-69) ou "F" (abaixo de 60).

print("====Notas====")

nota = float(input("informe sua nota de 0 a 100: "))

if  nota >= 90 and nota <= 100 :
    print(f"Sua classificação é a A") 
elif nota >= 80 and  nota <= 89:
    print(f"Sua classificação é a B") 
elif nota >= 70 and nota <= 79 :
    print(f"Sua classificação é a C")
elif nota >= 60 and nota <= 69 :
    print(f"Sua classificação é a D")   
elif nota <=60 :
    print(f"Sua classificção é a F")     
else :
    print("Sua nota máxima é 100")


print("ingrese una nota del 1 al 10: ")
nota = float(input())
if (nota>=0 and nota<=3):
    print("la nota es insuficiente")
else:
    if(nota>=4 and nota<=6):
        print("la nota es suficiente")
    elif(nota>=7 and nota <=10):
        print("la nota esta bien!")

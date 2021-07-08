numero1 = input("ingrese un numero entre el 1 y el 9: ")
numero2 = input("ingrese un numero entre el 1 y el 9: ")
numero3 = input("ingrese un numero entre el 1 y el 9: ")

print("el nombre de los numeros ingresados: ")
for i in "uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, 10":
    if i in numero1 or numero2 or numero3:
        print(i)
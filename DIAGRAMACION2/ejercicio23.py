menuPrincipal = int(input("Menu principal: \n 1-Sumar \n 2-Restar \n 3-Multiplicar \n 4-Dividir \n 5-Salir \n "))

while menuPrincipal != 0:
    if menuPrincipal == 1:
        print("usted pulso la operacion sumar")
    elif menuPrincipal == 2:
        print("usted pulso la operacion restar")
    elif menuPrincipal == 3:
        print("usted pulso la operacion multiplicar")
    elif menuPrincipal == 4:
        print("usted pulso la operacion dividir")
    elif menuPrincipal == 5:
        print("usted pulso para salir")
    else:
        print("Usted ingreso una opcion invalida")
    
    menuPrincipal = int(input("Menu principal: \n 1-Sumar \n 2-Restar \n 3-Multiplicar \n 4-Salir \n "))
comprobar = True

while comprobar == True:
    n = int(input("ingrese un numero entero positivo: "))

    if n > 0:
        i = 1
        while i < 11:
            print(n, "por", i, "es igual a: ", n*i)
            i += 1 
        comprobar = False

    else:
        print("el numero ingresado no es correcto. Intentelo de nuevo.")


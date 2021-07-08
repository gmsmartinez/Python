anio = int(input("ingrese el anio: "))
if anio > 2000 and anio < 2023:
        mes = int(input("ingrese el mes: "))
        if mes >=1 and mes <= 12:
            dias = int(input("ingrese la cantidad de dias: "))
            if dias == 28:
                print("el mes mes ingresado es febrero tiene 28 dias")
            elif dias == 30:
                print("el mes ingresado tiene 30 dias")
            elif dias == 31:
                print("el mes ingresado tiene 31 dias")
            else:
                print("no ingresaste un numero de dias valido") 
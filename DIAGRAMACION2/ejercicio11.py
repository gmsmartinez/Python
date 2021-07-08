anio = int(input("ingrese el anio: "))
if anio > 2000 and anio < 2023:
    dia = int(input("ingrese el dia: "))
    if dia >=1 and dia < 31: 
        mes = int(input("ingrese el mes: "))
        if mes >= 1 and mes <13: 
            print("la fecha ingresa es correcta")
        else: 
            print("el mes ingresado no es correcto") 



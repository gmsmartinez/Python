anio= int(input("Ingrese el año: "))
if anio > 2000 and anio < 2023:
    dia = int(input("Ingrese el dia: "))
    if dia >=1 and dia <31: 
        mes = int(input("Ingrese el mes: "))
        if mes >= 1 and mes < 13:  
            print(" La fecha ingresada es correcta")
        else:
            print("El mes ingresado no es correcto")
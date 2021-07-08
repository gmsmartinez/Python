print("Ingrese un numero entre 0 y 9.9999: ")
num = float(input())
if (num<0 or num>9.9999):
    print("el numero ingresado es invalido")
else: 
    if(num<10):
        print("el numero ingresa tiene 1 cifra")
    elif(num<100):
        print("el numero ingresado tiene 2 cifras")
    elif(num<1000):
        print("el numero ingresado tiene 3 cifras")
    elif(num<10000):
        print("el numero ingreado tiene 4 cifras")
    elif(num<100000):
        print("el numero ingresado tiene 5 cifras")
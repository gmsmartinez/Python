def sumaDigitos(num):
    s = 0
    while num > 0:
        s = s + num %10
        num = num // 10
    return s

n = int(input("cantidad de numeros: "))
sumaT = 0
while n > 0:
    num = int(input("Numero: "))
    sumaT = sumaT + sumaDigitos(num)
    n = n - 1

print("la suma de los digitos ingresados es " ,sumaT)
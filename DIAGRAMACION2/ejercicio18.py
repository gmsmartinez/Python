import random as rd

palabras =["Tomate", "Hielos", "Agosto", "Pintar", "Multar"]
indice=rd.randint(0,len(palabras)-1)
pal=palabras[indice]
palMayus=pal.upper()
letraPri=palMayus[0]
letraUlt=palMayus[-1]
n=len(palMayus)-2
subGuio=n* " _ "
pista= letraPri + subGuio + letraUlt
print(pista)
palUser=input("adivine la palabra: ").upper()
cond= palUser == palMayus
print("Gano?: " ,cond)
import os
os.system('cls')

a = float( input("Ingrese la variable a: ") )
b = float( input("Ingrese la variable b: ") )
c = float( input("Ingrese la variable c: ") )

if a < b < c:
    orden = "ascendente"
elif a > b > c:
    orden = "descendente"
else:
    orden = "desordenado"

print(f"Los números fueron ingresados en orden {orden}.")


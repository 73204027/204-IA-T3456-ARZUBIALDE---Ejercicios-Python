import os
import math

os.system('cls')

#Definir variables principales
r = float( input("Radio: ") )
h = float( input("Altura: "))

#Definir variables a calcular
area = 2 *math.pi * r * (r+h)
volumen = math.pi * r**2 * h

#Mostrar
print("Resultados:\n")
print(f"- Área Total = {area}u")
print(f"- Volumen = {volumen}u")
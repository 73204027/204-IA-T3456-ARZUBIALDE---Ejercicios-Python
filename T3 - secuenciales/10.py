import os
os.system('cls')

numero = int( input("Por favor, ingrese un número natural de 4 dígitos: ") )

#obtener cifras usando el operador de división entera por defecto:
cifra1 = numero // 1000
cifra2 = (numero % 1000) // 100
cifra3 = (numero % 100) // 10
cifra4 = numero % 10

#ordenar y formar el número al revés:
numero_al_reves = cifra4*1000 + cifra3*100 + cifra2*10 + cifra1

#Mostrar
print(f"El número al revés sería: {numero_al_reves}")
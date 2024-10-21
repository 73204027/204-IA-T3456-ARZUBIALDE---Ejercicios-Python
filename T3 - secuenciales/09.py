import os
os.system('cls')

numero = int( input("Por favor, ingrese un número natural de 4 dígitos: ") )

#obtener cifras usando el operador de división entera por defecto:
cifra1 = numero // 1000
cifra2 = (numero % 1000) // 100
cifra3 = (numero % 100) // 10
cifra4 = numero % 10

#calcular suma de cifras
suma = cifra1 + cifra2 + cifra3 + cifra4 

#Mostrar resultados
print(f"La suma de cifras es: {suma}")
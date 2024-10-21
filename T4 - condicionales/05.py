import os
os.system('cls')

# Solicitar un número de 4 cifras
numero = int( input("Ingrese un número natural de 4 cifras: ") )

# Obtener cifras usando el operador de división entera
cifra1 = numero // 1000
cifra2 = (numero % 1000) // 100
cifra3 = (numero % 100) // 10
cifra4 = numero % 10

# Crear una lista con las cifras
cifras = [cifra1, cifra2, cifra3, cifra4]

# Determinar la mayor y menor cifra
mayor_cifra = max(cifras)
menor_cifra = min(cifras)

# Formar el mayor número posible de dos cifras
numero_mayor = int(f"{mayor_cifra}{menor_cifra}")

# Mostrar resultados
print(f"\nEl mayor número posible de dos cifras es: {numero_mayor}")
 

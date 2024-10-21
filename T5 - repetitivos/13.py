import os
os.system('cls')
###################################


n = int( input("Ingrese un número entero: ") )

suma = 0


for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 != 0:
        suma += i

print(f"La suma de todos los números enteros múltiplos de 3 pero no de 5, menores o iguales a {n}, es: {suma}")


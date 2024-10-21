import os
os.system('cls')
########################################


def suma_multiplos(numero_actual, limite):
    if numero_actual > limite: 
        return 0

    suma_actual = 0
    if numero_actual % 3 == 0 and numero_actual % 5 != 0:
        suma_actual = numero_actual

    return suma_actual + suma_multiplos(numero_actual + 1, limite)

n = int(input("Ingrese un número entero: "))


resultado = suma_multiplos(1, n)

#mostrar
print(f"La suma de todos los números enteros múltiplos de 3 pero no de 5, menores o iguales a {n}, es: {resultado}")

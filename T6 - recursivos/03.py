import os
os.system('cls')

def contar_divisores(numero, divisor=1, contador=0):
    if divisor > numero:
        return contador
    elif numero % divisor == 0:
        return contar_divisores(numero, divisor + 1, contador + 1)
    else:
        return contar_divisores(numero, divisor + 1, contador)

# Solicitar datos
numero = int( input("Ingrese un número entero: ") )

# Llamar a la función recursiva
contador = contar_divisores(numero)

# Mostrar el resultado
print(f"El número {numero} tiene {contador} divisores.")

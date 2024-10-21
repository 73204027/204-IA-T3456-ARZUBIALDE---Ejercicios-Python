import os
os.system('cls')
#-3-3-3-3-3-3-3-3-3-3-3-3-3

#init

# Función recursiva para calcular el factorial
def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_factorial(n - 1)

# Solicitar datos
numero = int( input("Ingrese un número entero para calcular su factorial: ") )

# Calcular el factorial
resultado = calcular_factorial(numero)

# Mostrar el resultado
print(f"El factorial de {numero} es: {resultado}")

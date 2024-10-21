import os
os.system('cls')
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Solicitar datos
numero = int( input("Ingrese un número entero para calcular su factorial: ") )

# Inicializar
factorial = 1

# Calcular el factorial
for i in range(1, numero + 1):
    factorial *= i

# Mostrar el resultado
print(f"El factorial de {numero} es: {factorial}")


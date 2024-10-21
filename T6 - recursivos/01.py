import os
os.system('cls')

# Función recursiva para calcular el número de restas
def calcular_division(dividendo, divisor, n_restas=0):
    if dividendo < divisor:
        return n_restas, dividendo
    else:
        return calcular_division(dividendo - divisor, divisor, n_restas + 1)

# Solicitar valores
dividendo = float( input("Ingrese el dividendo: ") )
divisor = float( input("Ingrese el divisor: ") )

# Inicializar
dividendo_original = dividendo

# Llamar a la función recursiva
n_restas, resto = calcular_division(dividendo, divisor)

# Mostrar resultado 
print(f"El {divisor:.2f} cabe dentro de {dividendo_original:.2f} {n_restas} veces y el resto es {resto:.2f}.")

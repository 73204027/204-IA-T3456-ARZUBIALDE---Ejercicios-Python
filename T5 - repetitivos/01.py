import os
os.system('cls')

# Solicitar valores
dividendo = float( input("Ingrese el dividendo: ") )
divisor = float( input("Ingrese el divisor: ") )

# Inicializar
dividendo_original = dividendo
n_restas = int(0)

# Bucle para asegurar que las restas sucesivas se realizarán hasta que el resultado sea menor que el divisor
while dividendo >= divisor: 
    dividendo -= divisor
    n_restas += 1
else:
    resto = dividendo

# Mostrar resultado 
print(f"El {divisor:.2f} cabe dentro de {dividendo_original:.2f} {n_restas} veces y el resto es {resto:.2f}.")


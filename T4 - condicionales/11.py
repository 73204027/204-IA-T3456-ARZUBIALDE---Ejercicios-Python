import os
os.system('cls')

# Solicitar un número
numero = float( input("Ingrese un número: ") )

# Determinar el signo del número
if numero > 0:
    signo = "positivo"
elif numero < 0:
    signo = "negativo"
else:
    signo = "cero"

# Mostrar el resultado
print(f"El número ingresado es {signo}.")
 

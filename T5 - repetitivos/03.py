import os
os.system('cls')
##################################################################3333

# Solicitar datos
numero = int( input("Ingrese un número entero: ") )

# Inicializar
contador = 0


for i in range(1, numero + 1):
    if numero % i == 0:
        contador += 1

# Mostrar el resultado!
print(f"El número {numero} tiene {contador} divisores!")


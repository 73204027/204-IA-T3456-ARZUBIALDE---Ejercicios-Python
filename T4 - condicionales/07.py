import os
os.system('cls')

# Solicitar tres números enteros
numero1 = int( input("Ingrese el primer número entero: ") )
numero2 = int( input("Ingrese el segundo número entero: ") )
numero3 = int( input("Ingrese el tercer número entero: ") )

# Determinar el número intermedio
numero_intermedio = (numero1 + numero2 + numero3) - max(numero1, numero2, numero3) - min(numero1, numero2, numero3)

# Mostrar resultado
print(f"\nEl número intermedio es: {numero_intermedio}")


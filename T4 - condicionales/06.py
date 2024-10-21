import os
os.system('cls')

# Solicitar las tres edades
edad1 = int( input("Ingrese la primera edad: ") )
edad2 = int( input("Ingrese la segunda edad: ") )
edad3 = int( input("Ingrese la tercera edad: ") )

# Determinar la edad mayor y menor
edad_mayor = max(edad1, edad2, edad3)
edad_menor = min(edad1, edad2, edad3)

# Mostrar resultados
print(f"\nLa edad mayor es: {edad_mayor}")
print(f"La edad menor es: {edad_menor}")


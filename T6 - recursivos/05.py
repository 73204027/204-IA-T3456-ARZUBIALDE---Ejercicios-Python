import os
os.system('cls')

# Función recursiva para mostrar la tabla de multiplicar
def tabla_multiplicar(n, i=1):
    if i > 12:
        return
    print(f"{n} x {i} = {n * i}")
    tabla_multiplicar(n, i + 1)

# Solicitar datos
n = int( input("Ingrese el número n para generar su tabla de multiplicar: ") )

# Mostrar la tabla de multiplicar del 1 al 12
print(f"Tabla de multiplicar del {n}:")
tabla_multiplicar(n)

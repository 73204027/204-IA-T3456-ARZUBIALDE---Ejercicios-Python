import os
os.system('cls')
#########################3

def tabla(n, x, y):
    if x > y:
        return
    print(f"{n} x {x} = {n * x}")
    tabla(n, x + 1, y)

# Solicitar datos
n = int( input("Ingrese el número n para generar la tabla de multiplicar respectiva: ") )
x = int( input("Ingrese el valor inicial de la tabla (x): ") )
y = int( input("Ingrese el valor final de la tabla (y): ") )

# Mostrar la tabla de multiplicar del x al y
print(f"Tabla de multiplicar del {n}, desde {x} hasta {y}:")
tabla(n, x, y)

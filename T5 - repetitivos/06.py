import os
os.system('cls')
#- - - - - - - - - - - - - - - - - - - -- - - - - - - 


# Solicitar datos
n = int( input("Ingrese el número n para generar la tabla de multiplicar respectiva: ") )
x = int( input("Ingrese el valor inicial de la tabla (x): ") )
y = int( input("Ingrese el valor final de la tabla (y): ") )



# Mostrar la tabla de multiplicar del x al y
print(f"Tabla de multiplicar del {n}, desde {x} hasta {y}:")
for i in range(x, y + 1):
    print(f"{n} x {i} = {n * i}")


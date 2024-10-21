import os
os.system('cls')
#############################################################

# Solicitar datos
n = int( input("Ingrese el número n para generar la tabla de multiplicar respectiva: ") )



# Mostrar la tabla de multiplicar del 1 al 12
print(f"Tabla de multiplicar del {n}:")
for i in range(1, 13):
    print(f"{n} x {i} = {n * i}")


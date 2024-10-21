import os
os.system('cls')
##############################

# Solicitar datos
n = int( input("Ingrese el número n: ") )
m = int( input("Ingrese la cantidad de múltiplos m que desea mostrar: ") )

#Inicializar

# MOstrar
print(f"Los primeros {m} múltiplos de {n} son:")

# Mostrar resultados
for i in range(1, m + 1):
    print(f"{n * i}")


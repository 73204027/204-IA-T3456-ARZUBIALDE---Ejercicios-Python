import os
os.system('cls')
##############################

print("Números del 1 al 100:\n")

# Init
contador = 1

# Mostrar números del 1 al 100
for i in range(1, 101):
    print(f"{i:2}", end=" ")
    if contador % 10 == 0:  # Saltar a la sig linea
        print() 
    contador += 1


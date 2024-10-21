import os
os.system('cls')
###################

contador = 0

print("Números capicúas de 3 cifras:")


for numero in range(100, 1000):
    numero_str = str(numero)
    
    if numero_str == numero_str[::-1]:
        print(numero)
        contador += 1

# Mostrar 
print(f"\nCantidad de números capicúas de 3 cifras: {contador}")


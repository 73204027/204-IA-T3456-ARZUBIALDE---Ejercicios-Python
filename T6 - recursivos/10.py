import os
os.system('cls')
#---------------------------------------

def suma_cifras(numero, suma_pares=0, suma_impares=0):
    if numero == 0:
        return suma_pares, suma_impares
    else:
        cifra = numero % 10
        if cifra % 2 == 0:
            suma_pares += cifra
        else:
            suma_impares += cifra
        return suma_cifras(numero // 10, suma_pares, suma_impares)

# Inicializar 
contador = 0

print("Números de 4 cifras cuya suma de cifras pares es igual a la suma de cifras impares:")


for numero in range(1000, 10000):
    suma_pares, suma_impares = suma_cifras(numero)
    
    # Verificar la condición
    if suma_pares == suma_impares:
        print(numero)
        contador += 1

# Mostrar 
print(f"\nCantidad de números encontrados: {contador}")

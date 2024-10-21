import os
os.system('cls')
###################################

# Inicializar contador
contador = 0

print("Números de 4 cifras cuya suma de cifras pares es igual a la suma de cifras impares:")

for numero in range(1000, 10000):
    # Obtener cifras
    cifra1 = numero // 1000
    cifra2 = (numero % 1000) // 100
    cifra3 = (numero % 100) // 10
    cifra4 = numero % 10
    
    # Sumar cifras pares e impares
    suma_pares = 0
    suma_impares = 0
    
    for cifra in (cifra1, cifra2, cifra3, cifra4):
        if cifra % 2 == 0:
            suma_pares += cifra
        else:
            suma_impares += cifra
    
    # Verificar la condición
    if suma_pares == suma_impares:
        print(numero)
        contador += 1

# Mostrar resultados
print(f"\nCantidad de números encontrados: {contador}")


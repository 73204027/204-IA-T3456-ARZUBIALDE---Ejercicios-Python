import os
os.system('cls')

# Solicitar un número entero positivo de tres cifras
numero = int( input("Ingrese un número entero positivo de tres cifras: ") )

# Verificar que el número sea de 3 cifras!
if 100 <= numero <= 999:
    # Obtener las cifras
    cifra1 = numero // 100
    cifra2 = (numero % 100) // 10
    cifra3 = numero % 10

    # Determinar si se cumple condición
    if (cifra2 == cifra1 + 1 and cifra3 == cifra2 + 1) or (cifra2 == cifra1 - 1 and cifra3 == cifra2 - 1):
        print("Las cifras son consecutivas.")
    else:
        print("Las cifras no son consecutivas.") #Mostrar
else:
    print("El número ingresado no es un número entero positivo de tres cifras.") #Mostrar
    
 

import os
os.system('cls')
##########################################################################

def es_capicua(numero, longitud=None):
    if longitud is None:
        longitud = len(str(numero))
    if longitud <= 1:  # Caso base
        return True
    else:
        numero_str = str(numero)
        return numero_str[0] == numero_str[-1] and es_capicua(numero_str[1:-1], longitud - 2)

# Inicializar 
contador = 0

print("Números capicúas de 3 cifras:")
for numero in range(100, 1000):
    # Verificar si es capicúa
    if es_capicua(numero):
        print(numero)
        contador += 1

# Mostrar
print(f"\nCantidad de números capicúas de 3 cifras: {contador}")

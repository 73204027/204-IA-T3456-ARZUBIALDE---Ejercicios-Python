import os
os.system('cls')
#- - - - - - - - - - - - - - - - - - - -  - - - - - -  

def rectangulo_recursivo(altura):
    if altura > 0:
        print('*' * (2 * altura))
        rectangulo_recursivo(altura - 1)

# Solicitar datos
n = int(input("Ingrese la altura n del rectángulo (n >= 4): "))

# CONDICIÓN
if n >= 4:
    print("Rectángulo de asteriscos:")
    rectangulo_recursivo(n) #función recursiva
else:
    print("La altura debe ser al menos 4.")

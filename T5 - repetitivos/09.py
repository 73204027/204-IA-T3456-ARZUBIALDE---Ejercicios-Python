import os
os.system('cls')
#######################################3


# Solicitar datos
n = int( input("Ingrese la altura n del rectángulo (n >= 4): ") )

# Condición 
if n >= 4:
    #mostrar
    print("Rectángulo de asteriscos:") 
    for _ in range(n):
        print('*' * (2 * n))
else:
    #mostrar
    print("La altura debe ser al menos 4.")


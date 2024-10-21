import os
os.system('cls')

def multiplicar(num1, num2):
    if num2 == 0:
        return 0
    elif num2 < 0:
        return -multiplicar(num1, -num2)
    else:
        return num1 + multiplicar(num1, num2 - 1)

# Solicitar datos
print("Hola, estimado usuario.\nEste programa realiza la operación '*' mediante su definición fundamental: Sumas sucesivas")
num1 = int( input("Ingrese el primer número: ") )
num2 = int( input("Ingrese el segundo número: ") )

# Llamar a la función recursiva
resultado = multiplicar(num1, num2)

# Mostrar el resultado
print(f"El resultado de la multiplicación es: {resultado}")

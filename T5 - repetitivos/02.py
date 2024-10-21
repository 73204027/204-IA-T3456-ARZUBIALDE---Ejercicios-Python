import os
os.system('cls')

#Solicitar datos
print("Hola, estimado usuario.\nEste programa realiza la operación '*' mediante su definición fundamental: Sumas sucesivas")
num1 = int( input("Ingrese el primer número: ") )
num2 = int( input("Ingrese el segundo número: ") )

# Inicializar
resultado = 0

# Sumas sucesivas
for _ in range(abs(num2)):
    resultado += num1

# Regla de signos
if num2 < 0:
    resultado = -resultado

# Mostrar el resultado
print(f"El resultado de la multiplicación es: {resultado}")

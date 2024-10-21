import os
os.system('cls')

print("Por favor, ingrese dos números de 3 cifras:")

### Solicitar números
numero1 = int( input("Primer número: ") )
numero2 = int( input("Segundo número: ") )

# Obtener cifras de cada número
primera_cifra_1 = numero1 // 100
segunda_cifra_1 = (numero1 % 100) // 10
tercera_cifra_1 = numero1 % 10

primera_cifra_2 = numero2 // 100
segunda_cifra_2 = (numero2 % 100) // 10
tercera_cifra_2 = numero2 % 10

# Intercambiar la primer y tercer cifra
nuevo_numero1 = tercera_cifra_1 * 100 + segunda_cifra_1 * 10 + primera_cifra_2
nuevo_numero2 = tercera_cifra_2 * 100 + segunda_cifra_2 * 10 + primera_cifra_1

# Mostrar resultados
print(f"Los nuevos números son: {nuevo_numero1} y {nuevo_numero2}")

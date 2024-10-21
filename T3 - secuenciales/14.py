import os
os.system('cls')

print("Ingrese 5 números:")

### Solicitar 5 números
n1 = float( input("Primer número: ") )
n2 = float( input("Segundo número: ") )
n3 = float( input("Tercer número: ") )
n4 = float( input("Cuarto número: ") )
n5 = float( input("Quinto número: ") )

### Ordenar los números y seleccionar los 3 mayores
mayores = sorted([n1, n2, n3, n4, n5], reverse=True)[:3]

### Calcular promedio de los 3 mayores
promedio = sum(mayores) / 3

######### Mostrar resultados
print(f"El promedio de los 3 números mayores es: {promedio:.2f}")

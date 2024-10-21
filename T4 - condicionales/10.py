import os
os.system('cls')

# Solicitar las 5 notas
nota1 = float( input("Ingrese la primera nota: ") )
nota2 = float( input("Ingrese la segunda nota: ") )
nota3 = float( input("Ingrese la tercera nota: ") )
nota4 = float( input("Ingrese la cuarta nota: ") )
nota5 = float( input("Ingrese la quinta nota: ") )

# Almacenar las notas en una lista
notas = [nota1, nota2, nota3, nota4, nota5]

# Determinar la nota mayor y la menor
nota_mayor = max(notas)
nota_menor = min(notas)

# Mostrar las notas eliminadas
print(f"\nNotas eliminadas:\n- Mayor: {nota_mayor}\n- Menor: {nota_menor}")

# Calcular el promedio de las notas restantes
notas.remove(nota_mayor)  # Eliminar la nota mayor
notas.remove(nota_menor)   # Eliminar la nota menor
promedio = sum(notas) / len(notas)

# Mostrar el promedio
print(f"\nEl promedio aprobatorio es: {promedio:.2f}")
 

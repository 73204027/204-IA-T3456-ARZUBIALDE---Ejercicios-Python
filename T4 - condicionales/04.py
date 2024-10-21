import os
os.system('cls')

# Solicitar las notas de las tres prácticas
practica1 = float( input("Ingrese la nota de la primera práctica: ") )
practica2 = float( input("Ingrese la nota de la segunda práctica: ") )
practica3 = float( input("Ingrese la nota de la tercera práctica: ") )

# Incrementar la nota de la tercera práctica si es mayor o igual a 10
if practica3 >= 10:
    practica3 += 2

# Calcular el promedio final
promedio_final = (practica1 + practica2 + practica3) / 3

# Mostrar resultados
print(f"\nEl promedio final del alumno es: {promedio_final:.2f}")


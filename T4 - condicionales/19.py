import os
os.system('cls')

sexo = input("Ingrese el sexo del postulante (femenino/masculino): ").strip().lower()
edad = int( input("Ingrese la edad del postulante: ") )

if sexo == "femenino":
    if edad < 23:
        categoria = "FA"
    else:
        categoria = "FB"
elif sexo == "masculino":
    if edad < 25:
        categoria = "MA"
    else:
        categoria = "MB"
else:
    categoria = "Sexo no válido"

print(f"La categoría del postulante es: {categoria}")


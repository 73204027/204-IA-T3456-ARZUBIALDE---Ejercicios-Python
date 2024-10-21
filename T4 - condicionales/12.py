 import os
os.system('cls')

# Solicitar un número entero correspondiente a un día de la semana
dia = int( input("Ingrese un número del 1 al 7: ") )

# Determinar el nombre del día
if dia == 1:
    nombre_dia = "lunes"
elif dia == 2:
    nombre_dia = "martes"
elif dia == 3:
    nombre_dia = "miércoles"
elif dia == 4:
    nombre_dia = "jueves"
elif dia == 5:
    nombre_dia = "viernes"
elif dia == 6:
    nombre_dia = "sábado"
elif dia == 7:
    nombre_dia = "domingo"
else:
    nombre_dia = "invalido"

# Mostrar el resultado
if nombre_dia != "invalido":
    print(f"El día correspondiente es: {nombre_dia}.")
else:
    print("El número ingresado no corresponde a un día de la semana.")


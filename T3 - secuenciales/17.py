import os
os.system('cls')

print("Ingrese el monto total de la donación anual:")

# Solicitar monto de la donación
donacion_total = float( input("Monto de la donación en soles: ") )

# Calcular distribución
centro_salud = donacion_total * 0.25
comedor_infantil = donacion_total * 0.35
escuela_infantil = donacion_total * 0.25
asilo_ancianos = donacion_total - (centro_salud + comedor_infantil + escuela_infantil)

#Mostrar resultados
print(f"Centro de salud recibe: S/. {centro_salud:.2f}")
print(f"Comedor infantil recibe: S/. {comedor_infantil:.2f}")
print(f"Escuela infantil recibe: S/. {escuela_infantil:.2f}")
print(f"Asilo de ancianos recibe: S/. {asilo_ancianos:.2f}")

import os
os.system('cls')

# Solicitar la cantidad de exámenes aprobados
examenes_aprobados = int( input("Ingrese la cantidad de exámenes aprobados: ") )

# Propina base mensual
propina_base = 20
# Propina adicional por examen aprobado
propina_adicional_por_examen = 5

# Calcular monto total de la propina
monto_total_propina = propina_base + (propina_adicional_por_examen * examenes_aprobados)

# Mostrar resultado
print(f"\nEl monto total de la propina es: S/. {monto_total_propina}")


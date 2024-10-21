import os
os.system('cls')

# Solicitar el ingreso mensual y el costo de la casa
ingreso_mensual = float( input("Ingrese el ingreso mensual: S/. ") )
costo_casa = float( input("Ingrese el costo de la casa: S/. ") )

# Inicializar variables
cuota_inicial = 0
cuota_mensual = 0

# Verificar las condiciones para calcular la cuota inicial y el monto de la cuota mensual
if ingreso_mensual < 1250:
    cuota_inicial = 0.15 * costo_casa  # 15% del costo de la casa
    monto_financiar = costo_casa - cuota_inicial
    cuota_mensual = monto_financiar / 120  # Distribuido en 120 cuotas
else:
    cuota_inicial = 0.30 * costo_casa  # 30% del costo de la casa
    monto_financiar = costo_casa - cuota_inicial
    cuota_mensual = monto_financiar / 75  # Distribuido en 75 cuotas

# Mostrar la cuota inicial y el monto de la cuota mensual
print(f"Cuota inicial: S/. {cuota_inicial:.2f}")
print(f"Monto de la cuota mensual: S/. {cuota_mensual:.2f}")


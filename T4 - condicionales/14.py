import os
os.system('cls')

# Solicitar el número de la tarjeta y el monto de la compra
numero_tarjeta = int( input("Ingrese el número de la tarjeta: ") )
monto_compra = float( input("Ingrese el monto de la compra: S/. ") )

# Inicializar la variable de descuento
descuento = 0

# Verificar si el número de la tarjeta es par y no menor de 100
if numero_tarjeta >= 100 and numero_tarjeta % 2 == 0:
    descuento = 0.15 * monto_compra  # 15% de descuento
else:
    descuento = 0.05 * monto_compra  # 5% de descuento

# Mostrar el número de la tarjeta, el monto de la compra y el descuento
print(f"Número de la tarjeta: {numero_tarjeta}")
print(f"Monto de la compra: S/. {monto_compra:.2f}")
print(f"Descuento: S/. {descuento:.2f}")


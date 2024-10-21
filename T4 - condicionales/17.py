import os
os.system('cls')

# solicitar
docenas = int( input("Ingrese la cantidad de docenas compradas: ") )

# precio por docena
precio_por_docena = 30  # Precio fijo por docena, puedes cambiarlo si es necesario

# calcular monoto
monto_compra = docenas * precio_por_docena

# init
descuento = 0
lapiceros = 0

# Calcular descuento
if docenas >= 6:
    descuento = 0.15 * monto_compra  # 15% de descuento
else:
    descuento = 0.10 * monto_compra  # 10% de descuento

# Calcular la cantidad de lapiceros de obsequio
if docenas >= 30:
    lapiceros = (docenas // 3) * 2  # 2 lapiceros por cada 3 docenas

# total
total_a_pagar = monto_compra - descuento

# Mostrar resultados
print(f"Monto de la compra: S/. {monto_compra:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Total a pagar: S/. {total_a_pagar:.2f}")
print(f"Cantidad de lapiceros de obsequio: {lapiceros}")


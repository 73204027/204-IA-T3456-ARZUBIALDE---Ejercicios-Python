import os
os.system('cls')

# Solicitar cantidad de unidades
cantidad = int( input("Ingrese la cantidad de unidades adquiridas: ") )

# Definir el precio unitario según la cantidad
if cantidad >= 1 and cantidad <= 25:
    precio_unitario = 27
elif cantidad >= 26 and cantidad <= 50:
    precio_unitario = 25
elif cantidad >= 51:
    precio_unitario = 23
else:
    precio_unitario = 0  # Para el caso de cantidades no válidas

# Calcular el importe de la compra
importe = cantidad * precio_unitario

# Determinar el descuento
if cantidad > 50:
    descuento = importe * 0.15
else:
    descuento = importe * 0.05

# Calcular el total a pagar
total_pagar = importe - descuento

# Mostrar resultados
print(f"\nImporte de la compra: S/. {importe:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Total a pagar: S/. {total_pagar:.2f}")


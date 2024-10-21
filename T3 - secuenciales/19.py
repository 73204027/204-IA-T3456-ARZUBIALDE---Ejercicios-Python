import os
os.system('cls')

print("Cálculo del sueldo de un vendedor:")

#Solicitar monto vendido
monto_vendido = float( input("Monto total vendido: ") )

#Calcular sueldo, comisión y descuentos
sueldo_basico = 500
comision = monto_vendido * 0.09
sueldo_bruto = sueldo_basico + comision
descuento = sueldo_bruto * 0.11
sueldo_neto = sueldo_bruto - descuento

#Mostrar
print(f"Sueldo básico: S/. {sueldo_basico:.2f}")
print(f"Comisión: S/. {comision:.2f}")
print(f"Sueldo bruto: S/. {sueldo_bruto:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Sueldo neto: S/. {sueldo_neto:.2f}")

import os
os.system('cls')

print("Ingrese los datos de la compra:")

#Solicitar cantidad y precio unitario
cantidad = int( input("Cantidad de unidades: ") )
precio_unitario = float( input("Precio unitario: ") )

#Calcular importe de la compra y descuentos
importe_compra = cantidad * precio_unitario
primer_descuento = importe_compra * 0.15
importe_con_descuento = importe_compra - primer_descuento
segundo_descuento = importe_con_descuento * 0.15
importe_final = importe_con_descuento - segundo_descuento

#Mostrar resultados
print(f"Importe de la compra: S/. {importe_compra:.2f}")
print(f"Descuento total: S/. {(primer_descuento + segundo_descuento):.2f}")
print(f"Importe a pagar: S/. {importe_final:.2f}")

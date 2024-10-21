import os
os.system('cls')

donacion = float( input("Ingres el monto de la donación: ") )

if donacion >= 10000:
    centro_salud = donacion * 0.30
    comedor_ninos = donacion * 0.50
else:
    centro_salud = donacion * 0.25
    comedor_ninos = donacion * 0.60

inversion_bolsa = donacion - (centro_salud + comedor_ninos)

print(f"Destinos de la donación:\n- Centro de salud: ${centro_salud:.2f}\n- Comedor de niños: ${comedor_ninos:.2f}\n- Inversión en la bolsa: ${inversion_bolsa:.2f}")

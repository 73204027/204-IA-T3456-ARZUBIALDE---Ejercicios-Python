import os
os.system('cls')
#----------------------------------------------------------

valor = float( input("Ingrese la medición en metros:") )

fc_cm = 100
fc_pulgadas = 39.37 
fc_pies = 3.28
fc_yardas = 1.09

print("Esa medición equivale a:\n ")
print(f"{valor*fc_cm:.2f} centímetros.")
print(f"{valor*fc_pulgadas:.2f} pulgadas.")
print(f"{valor*fc_pies:.2f} pies.")
print(f"{valor*fc_yardas:.2f} yardas.")


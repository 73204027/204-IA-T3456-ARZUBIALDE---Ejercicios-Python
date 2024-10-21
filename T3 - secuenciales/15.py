import os
os.system('cls')

print("Ingrese los aportes de Juan, Rosa y Daniel:")

#### Solicitar aportes
aporte_juan = float( input("Aporte de Juan en dólares: ") )
aporte_rosa = float( input("Aporte de Rosa en dólares: ") )
aporte_daniel = float( input("Aporte de Daniel en soles: ") )

# Convertir el aporte de Daniel a dólares
fc_soles_dolares = 3.00
aporte_daniel_dolares = aporte_daniel / fc_soles_dolares

#Calcular capital total
capital_total = aporte_juan + aporte_rosa + aporte_daniel_dolares

#Calcular porcentajes
porcentaje_juan = (aporte_juan / capital_total) * 100
porcentaje_rosa = (aporte_rosa / capital_total) * 100
porcentaje_daniel = (aporte_daniel_dolares / capital_total) * 100

# Mostrar
print(f"El capital total es: ${capital_total:.2f}")
print(f"Juan aporta el {porcentaje_juan:.2f}%, Rosa el {porcentaje_rosa:.2f}% y Daniel el {porcentaje_daniel:.2f}%")

import os
os.system('cls')

print("Cálculo del sueldo de un empleado:")

# Solicitar datos
horas_trabajadas = float( input("Horas trabajadas: ") )
tarifa_horaria = float( input("Tarifa por hora: ") )

# Calcular sueldo básico, bruto y neto
sueldo_basico = horas_trabajadas * tarifa_horaria
sueldo_bruto = sueldo_basico * 1.20  # 20% bonificación
sueldo_neto = sueldo_bruto * 0.90  # 10% descuento

# Mostrar
print(f"Sueldo básico: ${sueldo_basico:.2f}")
print(f"Sueldo bruto: ${sueldo_bruto:.2f}")
print(f"Sueldo neto: ${sueldo_neto:.2f}")

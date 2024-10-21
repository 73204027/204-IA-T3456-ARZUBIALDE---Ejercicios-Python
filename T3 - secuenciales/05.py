import os
os.system('cls')

#solicitar al usuario
capacidad_GB = float( input("Capacidad del disco(GB): "))

#definir factores de conversión:
fc__GB_MB = 1024    
fc__GB_KB = 1024**2 #1024*1024
fc__GB_B = 1024**3 #1024*1024*1024

#Convertir a las unidades respectivas
capacidad_MB = capacidad_GB *fc__GB_MB
capacidad_KB = capacidad_GB *fc__GB_KB
capacidad_B = capacidad_GB *fc__GB_B

#Mostrar
print(f"{capacidad_GB}GB equivalen a:")
print(f"- {capacidad_MB} MegaBytes")
print(f"- {capacidad_KB} KiloBytes")
print(f"- {capacidad_B} Bytes")
print("\n")
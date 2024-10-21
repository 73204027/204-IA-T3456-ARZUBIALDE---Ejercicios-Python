import os
os.system('cls')

#establecer factores de conversión a partir de los datos proporcionados:

#a metros:
fc__km_m = 1000 
fc__pies_m = 1/3.2808111 #sale de los valores del documento
fc__millas_m = 1609

#a yardas:
fc__m_yardas = 1/3*3.2808 #sale de los valores del documento

#solicitar medidas
print(" A continuación, ingrese las medidas correspondientes: ")
tramo1_km = float( input("Primer tramo(km): ") )
tramo2_pies = float( input("Segundo tramo(pies): ") )
tramo3_millas = float( input("Tercer tramo(millas): ") )

#Convertir todo a metros
tramo1_m = tramo1_km * fc__km_m
tramo2_m = tramo2_pies * fc__pies_m
tramo3_m = tramo3_millas * fc__millas_m

#Calcular el total (sumar todo)
TOTAL_m = tramo1_m + tramo2_m + tramo3_m

#También, convertir el TOTAL a yardas
TOTAL_yardas = TOTAL_m * fc__m_yardas

#Mostrar
print(f"\nLongitud total recorrida:\n{TOTAL_m:.2f} metros.\n{TOTAL_yardas:.2f} yardas.")



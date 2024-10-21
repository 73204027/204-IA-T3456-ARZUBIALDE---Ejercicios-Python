import os
os.system('cls')

#input
print("=================================================")
print("Por favor, ingrese su estatura en formato inglés:")
print("=================================================")
estatura_pies = int( input("Pies(´): "))
estatura_pulgadas = int( input("Pulgadas(´´): "))
print("\n")

#definir factores de conversión a metros:
fc__pies_m = 1/3.2808
fc__pulgadas_m = 2.54/100

#calcular estatura 
estatura = (estatura_pies*fc__pies_m) + (estatura_pulgadas*fc__pulgadas_m)

#mostrar
print(f"Usted mide {estatura:.2f} metros.")
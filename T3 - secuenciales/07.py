import os
os.system('cls')

print("Bienvenido!")
print("En este programa se calculará el área y el perímetro del rectángulo.")
print("Por favor, ingrese los valores:")

#Definir variables independientes:
b = float( input("Base: ") )
h = float( input("Altura: ") )


#Calcular área y perímetro en función de los datos introducidos:
area = b * h
perimetro = 2 * (b + h)

#Mostrar
print("\nResultados: ")
print(f"- Área = {area:.2f}u")
print(f"- Perímetro = {perimetro:.2f}u")
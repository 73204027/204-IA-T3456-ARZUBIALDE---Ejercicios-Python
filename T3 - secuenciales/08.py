import os
import math

os.system('cls')

#Mensaje al usuario
print("Estimado profesor, identifico un error en la siguiente definición presente en el documento:\nAREA TOTAL = 2 * a_base * a_lateral\nPara este ejercicio usé la definición correcta del área total, la cual es:\nAREA TOTAL = (2*a_base) + a_lateral")
print("=======================================================")
print("Bienvenido!")
print("En este programa se calculará el área de las bases, área lateral y área total del cilindro.")
print("Por favor, ingrese los valores:")

#Definir variables independientes:
r = float( input("Radio: ") )
h = float( input("Altura: "))


#Calcular variables dependientes en función de los datos ingresados
a_base = math.pi * r**2
a_lateral = 2 * math.pi * r * h
area = (2 * a_base) + a_lateral

#Mostrar
print("\nResultados: ")
print(f"- Área de la base = {a_base:.2f}u")
print(f"- Área lateral = {a_lateral:.2f}u")
print(f"- Área total = {area:.2f}u")
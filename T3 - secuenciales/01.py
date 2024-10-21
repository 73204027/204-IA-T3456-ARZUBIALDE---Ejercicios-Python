import os
os.system('cls')

varones = int( input("Cuántos hombres hay?: "))
mujeres = int( input("Cuántas mujeres hay?: "))

suma = varones + mujeres

varones_porcentaje = int( (varones/suma)*100 )
mujeres_porcentaje = 100 - varones_porcentaje #escojo esta manera, por que si usara la relación: (mujeres/suma)*100, es posible que, al convertirlo a int, se redondee y la suma del porcentaje de varones y el porcentaje de mujeres no de exactamente 100%

print(f"Los varones representan el {varones_porcentaje}% del grupo")
print(f"Las mujeres representan el {mujeres_porcentaje}% del grupo")
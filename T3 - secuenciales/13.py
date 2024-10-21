import os
os.system('cls')

print("Cálculo de la hipotenusa de un triángulo rectángulo:")

#Solicitar catetos
cateto1 = float( input("Ingrese el valor del primer cateto: ") )
cateto2 = float( input("Ingrese el valor del segundo cateto: ") )

#Calcular hipotenusa
hipotenusa = (cateto1**2 + cateto2**2)**0.5

# ,ostrar resultados
print(f"La hipotenusa es: {hipotenusa:.2f}")

import os
os.system('cls')

print("Resolución de la ecuación cuadrática ax^2 + bx + c:")

# SOLICITAR COEFICIENTES AL USUARIO
a = float( input("Ingrese el valor de 'a': ") )
b = float( input("Ingrese el valor de 'b': ") )
c = float( input("Ingrese el valor de 'c': ") )

# CALCULAR discriminante
discriminante = b**2 - 4*a*c

# CALCULAR SOLUCIONES
x1 = (-b + discriminante**0.5) / (2*a)
x2 = (-b - discriminante**0.5) / (2*a)

# MOSTRAR
print(f"Las soluciones son: {x1:.2f} y {x2:.2f}")

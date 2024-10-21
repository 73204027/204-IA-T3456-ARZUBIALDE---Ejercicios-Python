import os
os.system('cls')
############### #############################33

# Solicitar datos
n = float( input("Ingrese la base: ") )
m = int( input("Ingrese el exponente: ") )

# Inicializar 
potencia = 1

# Calcular la potencia
for _ in range(abs(m)):
    potencia *= n

# Regla de signos
if m < 0:
    potencia = 1 / potencia

# Mostrar el resultado
print(f"{n} elevado a {m} es: {potencia}")


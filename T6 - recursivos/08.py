import os
os.system('cls')
#######################################

def calcular_potencia(base, exponente):
    #casos
    if exponente == 0:
        return 1
    elif exponente < 0:
        return 1 / calcular_potencia(base, -exponente)
    else:
        return base * calcular_potencia(base, exponente - 1)

# Solicitar datos
n = float( input("Ingrese la base: ") )
m = int( input("Ingrese el exponente: ") )

# Calcular la potencia
resultado = calcular_potencia(n, m)

# Mostrar el resultado
print(f"{n} elevado a {m} es: {resultado}")

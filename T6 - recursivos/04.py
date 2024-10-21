import os
os.system('cls')
#######################

def multiplos_print(n, m, contador=1):
    if contador > m:
        return
    print(f"{n * contador}")
    multiplos_print(n, m, contador + 1)

# Solicitar datos
n = int( input("Ingrese el número n: ") )
m = int( input("Ingrese la cantidad de múltiplos m que desea mostrar: ") )

# Mostrar resultados
print(f"Los primeros {m} múltiplos de {n} son:")
multiplos_print(n, m)

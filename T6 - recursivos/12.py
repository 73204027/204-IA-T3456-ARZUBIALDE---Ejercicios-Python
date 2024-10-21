import os
os.system('cls')

# Función recursiva para mostrar números
def mostrar_numeros(numero_actual, limite, contador):
    print(f"{numero_actual:2}", end=" ")
    if contador % 10 == 0:  # Al llegar a 10 números, saltar a la siguiente línea
        print()  # Salto de línea
    if numero_actual < limite:  # Condición recursiva
        mostrar_numeros(numero_actual + 1, limite, contador + 1)

print("Números del 1 al 100, mostrando 10 números por fila:\n")

# Llamar a la función recursiva comenzando desde 1
mostrar_numeros(1, 100, 1)

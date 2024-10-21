import os
os.system('cls')
#-----------------------------------------------------------------------------------

#A
def convertir_a_mayusculas(texto, index=0):
    if index == len(texto):  # Condición de parada
        return ""
    letra = texto[index]
    return letra.upper() + convertir_a_mayusculas(texto, index + 1)  # Llamada recursiva


#B
def convertir_a_minusculas(texto, index=0):
    if index == len(texto):  # Condición de parada
        return ""
    letra = texto[index]
    return letra.lower() + convertir_a_minusculas(texto, index + 1)  # Llamada recursiva

texto = input("Ingresar texto: ")


texto_mayusculas = convertir_a_mayusculas(texto)
texto_minusculas = convertir_a_minusculas(texto)


#MOSTRAR 
print(f"Texto en mayúsculas: {texto_mayusculas}")
print(f"Texto en minúsculas: {texto_minusculas}")

import os
os.system('cls')
#--------------------------------------------------------------------------------

def es_primo(numero, divisor=2):
    if numero <= 1:  
        return False
    if divisor * divisor > numero:  
        return True
    if numero % divisor == 0:  
        return False
    return es_primo(numero, divisor + 1)  

numero = int(input("Ingrese un número entero: "))

#Qué mostrar?
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")

import os
os.system('cls')

#Solicitar cantidad
cantidad = int( input('Ingresar una cantidad de dinero: ') )

#Realizar divisiones enteras consecutivas

billetes_200 = cantidad // 200
cantidad = cantidad % 200 


billetes_100 = cantidad // 100
cantidad = cantidad % 100

billetes_50 = cantidad // 50
cantidad = cantidad % 50

billetes_20 = cantidad // 20
cantidad = cantidad % 20

billetes_10 = cantidad // 10
cantidad = cantidad % 10

monedas_5 = cantidad // 5
cantidad = cantidad % 5

monedas_2 = cantidad // 2
cantidad = cantidad % 2

monedas_1 = cantidad // 1
cantidad = cantidad % 1

#Mostrar resultados
print('Esa cantidad equivale a: ', end='\n\n')
print(f'{billetes_200} billetes de 200 soles.')
print(f'{billetes_100} billetes de 100 soles.')
print(f'{billetes_50} billetes de 50 soles.')
print(f'{billetes_20} billetes de 20 soles.')
print(f'{billetes_10} billetes de 10 soles')
print(f'{monedas_5} monedas de 5 soles.')
print(f'{monedas_2} monedas de 2 soles.')
print(f'{monedas_1} monedas de 1 sol.')
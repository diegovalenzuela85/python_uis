# EJERCICIO 04 - Realizar un programa que solicite un rango para generar 10 números de los cuales se debe
# identificar cual es el mayor y el menor

# import random
from random import randint
rango1 = int(input('Ingrese el primer dato del rango: '))
rango2 = int(input('Ingrese el segundo dato del rango: '))
numero = 0
llegada = []
for i in range(10):
    numero = randint(rango1,rango2)
    llegada.append(numero)
print(llegada)
min = min(llegada)
max = max(llegada)
print(f'El valor minimo es: {min} y el valor maximo es: {max}')
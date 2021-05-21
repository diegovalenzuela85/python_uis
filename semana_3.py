# EJERCICIOS SEMANA 3 - WHILE - FOR

'''

i = int(input('escriba un numero: '))
while i > 0:
    print(i)
    i = i - 1

estado = input('QUieres hacer una compra? (si / no): ')
if estado == 'si':
    numC = int(input('Cuantos articulos vas a comprar? '))
    acumulador = 0
    contador = 0
    while contador < numC:
        cant = int(input('Cuantos productos vas a comprar: '))
        precio = int(input('Ingresa el valor de un producto: '))
        precio_total_producto = cant * precio
        contador = contador + 1
        acumulador = acumulador + precio_total_producto

    print(f'El total a pagar es de = {acumulador}')
else:
    print('Adios')



# Pida un numero y si es positivo realice efectue la raiz cuadrada // Recuerde utilizar la funcion sqrt
# de la libreria math y para establecer desimales :.2f

import math
numero = int(input('Escriba un numero para sacarle la raiz cuadrada por favor: '))

while numero < 0:
    numero= int(input('ERROR -- Por favor escriba un numero positivo... -: '))

raiz = math.sqrt(numero)
print(f'la raiz cuadrada de {numero} es {raiz}')



# Pida un numero y escriba el acumulado descendente hasta llegar a cero

numero = int(input('Escribe un numero positivo: '))

while numero < 0:
    numero = int(input('ERROR---- Por favor escribe un numero positivo: '))

while numero > 0:
    print(numero)
    numero -= 1



# Preguntar que si deseas continuar condicionando a sí o no y se repita hasta que el usuario responda no.
# Tener en cuenta la palabra sí en minusculas y con tilde

pregunta = input('Deseas continuar?... (sí/no): ')

while pregunta == 'sí':
    pregunta = input('Por favor respondeme si deseas continuar?... (sí/no): ')
print('Correcto.... Muchas gracias')



# Debes ingresar una contraseña y confirmarla. Si no coincide con la primera que se ingreso,
# debe segir solicitandola hasta que sean las dos iguales

password_1 = input('Escribe tu contraseña: ')
password_2 = input('Confirma tu contraseña por favor: ')

while password_1 != password_2:
    password_2 = input('ERROR NO COINCIDE CON TU CONTRASEÑA---- Escribe nuevamente tu contraseña por favor: ')
print(f'\n\nMuchas gracias... \nTu contraseña es {password_1}')



# Vamos a crear una alcancia. Inicialmente debemos pedir cuanto desea ahorrar el usuario, y luego debe ir
# ingresando montos al ahorro hasta completar la cantidad que se desea ahorrar.
# el monto final puede ser igual o superior a la cantidad que se ingreso como monto a ahorrar.

monto_ahorrar = float(input('Cuanto dinero deseas ahorrar: '))
ingreso = 0
ahorro = 0

while ahorro <= monto_ahorrar:
    ingreso = float(input('Cuanto deseas ingresar a tu alcancia: '))
    print(f'Has ingresado a tu alcancia {ingreso} mas {ahorro} que tienes ya ahorrado. Por un total de {ingreso + ahorro}')
    ahorro += ingreso
print(f'\nFelicidades... Tu ingreso total es de {ahorro}')



# Se debe solicitar dos numeros enteros, el programa debe pedir el segundo numero mientras no sea mayor que el primero.
# Por ultimo debe mostrar los dos numeros

num1 = int(input('Ingresa un numero entero: '))
num2 = int(input('Ingresa un numero entero: '))

while num1 > num2:
    num2 = int(input('No es mayor que el primero. Ingresa un numero entero: '))
print(f'El primer nummro que ingresaste es {num1} y el segundo numero que ingresaste es {num2}')



# Se debe solicitar dos numeros enteros mientras no escriba un numero negativo. El programa terminara escribiendo
# la suma de los nuemros introducidos

num1 = 0
num2 = 0

while num1 >= 0 and num2 >= 0:
    num1 = int(input('Ingresa un numero entero: '))
    num2 = int(input('Ingresa un numero entero: '))
    if num1 > 0 and num2 > 0:
        print(f'Escribiste num1 = {num1} y num2 = {num2} - La Suma de los dos numeros es {num1 + num2}')

print('Lo siento... Escribiste uno o dos numeros negativos')



# Escriba un programa que pida primero dos numeros enteros (Minimo y maximo). Y despues debe pedir numeros enteros que
# esten situados entre ellos el programa terminara cuando se escriba un numero que no este en el rango. Al final
# debe escribir la cantidad de numeros escritos

print('Vamos a establecer un rango especifico')
rango_minimo = int(input('Escribe numero minimo que va tener el rango: '))
rango_maximo = int(input('Escribe numero maximo que va tener el rango: '))
num = int(input('Escribe un numero entero: '))
acumulado = ''

while rango_minimo <= num <= rango_maximo:
    acumulado = f"{acumulado} ({num}) "
    num = int(input('Escribe un numero entero: '))

print(f'Los numeros escritos durante el ingreso fueron: {acumulado}')
print(f'Lo siento... Escribiste un numero fuera del rango dado {rango_minimo,rango_maximo} <-> {num}')



# Escriba un programa que pida numeros pares mientras el usuario indique que quiere seguir introduciendo numeros.
# Para indicar que quiere seguir escribiendo numeros, el usuario debera contestar S o s a la pregunta.

aprobacion = input('Quieres identificar pares? ')

while aprobacion == 'S' or aprobacion == 's':
    num1 = int(input('Escribe un numero par por favor: '))
    num2 = int(input('Escribe otro numero par por favor: '))
    if num1 % 2 == 0 and num2 % 2 == 0:
        print(f'Correcto... Ingresaste dos numeros pares {num1} y {num2}')
        aprobacion = input('Quieres seguir introduciendo numeros para verificación? ')
    else:
        aprobacion = 'n'
        print('Ingresaste numeros impares... vuelve a intentarlo')

print('\nMuchas gracias por utilizar el programa.')

'''

# Escriba un programa que calcule si un numero es primo o no



# Escriba un programa que calcule la descomposicion de factores primos de un numero



# Escriba un algoritmo que calcule e imprima la suma de los n primeros numeros enteros positivos.
# El valor n debe leerse del teclado y ser ingresado por el usuario


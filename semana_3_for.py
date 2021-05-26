# for i in range(3):
#     print(i)

# for i in range(1,6):
#     print(f'Se ha agregado una manzana a la canasta. Ahora hay {i} manzanas')

# for i in range(1,6,3):
#     print(f'Se ha agregado una manzana a la canasta. Ahora hay {i} manzanas')

# for i in range(10,-1,-1):
#     print(f'Se ha agregado una manzana a la canasta. Ahora hay {i} manzanas')

# for i in range(0,10):
#     print(f'Se ha agregado una manzana a la canasta. Ahora hay {i} manzanas')

# for i in 'DIEGO':
#     print(f'Tu nombre es {i}')

# inicio = int(input('Ingrese el valor de inicio del ciclo: '))
# fin = int(input('Ingrese el valor de finalización del ciclo: '))
# paso = int(input('Ingrese el valor de cambio o paso del ciclo: '))
#
# print('Se ha iniciado el carrito. En total hay: 0 manzanas.')
#
# for i in range(inicio, fin, paso):
#     print(f'Se ha agregado manzanas a la canasta. Ahora tenemos {i} manzanas')

# inicio = int(input('Ingrese el valor de inicio del ciclo: '))
# fin = int(input('Ingrese el valor de finalización del ciclo: '))
# paso = int(input('Ingrese el valor de cambio o paso del ciclo: '))
#
# print('Se ha iniciado el carrito. En total hay: 0 manzanas.')
#
# for i in range(fin):
#     print(f'Se ha agregado manzanas a la canasta. Ahora tenemos {i} manzanas')

# nombre = 'DIEGO'
#
# for i in nombre:
#     print(f'{i}',end='   ')

# print('Comienzo')
# for i in [0, 1, 2]:
#     # print('Hola',i)
#     print(f'Hola {i}')
#
# print()
# print('Final')


# print('Comienzo')
# for i in ['Pedro','Juan','Fernando', 2]:
#     # print('Hola',i)
#     print(f'Hola {i}')
#
# print()
# print('Final')


# EJEMPLOS FOR PDF -------------------------------------------------------------------------------

# print('Comienzo')
# for i in [0,1,2]:
#     print(f'Hola {i}')
# print()
# print('Final')


# print('Comienzo')
# for i in []:
#     print(f'Hola')
# print()
# print('Final')


# print('Comienzo')
# for i in [1,1,1]:
#     print(f'Hola {i}')
# print()
# print('Final')


# print('Comienzo')
# for _ in [0,1,2]:
#     print(f'Hola')
# print()
# print('Final')


# print('Comienzo')
# for i in [3,4,5]:
#     print(f'Hola. Ahora i vale {i} y su cuadrado es {i**2}')
# print('Final')


# print('Comienzo')
# for i in ["Alba","Benito",27]:
#     print(f'Hola. Ahora i vale {i}')
# print('Final')


# print('Comienzo')
# for numero in [0,1,2,3]:
#     print(f'{numero} * {numero} = {numero**2}')
# print('Final')

# i = 10
# print(f'El bucle no ha comenzado. Ahora i vale {i}')
# for i in [0,1,2,3,4]:
#     print(f'{i} * {i} = {i**2}')
# print(f'El bucle ha terminado. Ahora i vale {i}')


# for i in "AMIGO":
#     print(f'Dame una {i}')
# print('¡AMIGO!')


# print('Comienzo')
# for numero in range(3):
#     print(f'Hola ',end='')
# print()
# print('Final')


# print('Comienzo')
# for i in range(10):
#     print(f'Hola ',end='')
# print()
# print('Final')


# print('Comienzo')
# for i in range(5):
#     print(f'Hola ',end='')
# print()
# print('Adiós')


# for i in [0,1,2]:
#     for j in [0,1]:
#         print(f'i vale {i} y j vale {j}')


# for i in range(3):
#     print(f'i (externa) vale {i}')
#     for i in range(2):
#         print(f'i (interna) vale {i}')


# for i in [1,2,3]:
#     for j in range(i):
#         print(f'i vale {i} y j vale {j}')


# EJERCICIOS PDF ---------------------------------------------------------------------------------------------

# 01 - Dado un numero generar su tabla de multiplicación

# num = int(input('Introduce un numero por favor: '))
# for i in range(1,11):
#     print(f'{num} * {i} = {num * i}')

# 02 - Dado un numero generar su factorial

# num = int(input('Ingresa un numero: '))
# factorial = 1
# acumulado = ''
# for i in range(1,num + 1):
#     factorial *= i
#     if i == 1:
#         acumulado = f"{acumulado} {i} "
#     else:
#         acumulado = f"{acumulado} * {i} "
# print(f'El factorial de {num}! es {acumulado} = {factorial}')


# 03 - Escriba un programa que pida un número y me calcule el Fibonacci.

# num = int(input('Escriba un numero para calcular el Fibonacci: '))
# if num < 0:
#     print('ERROR-------> Ingresaste un numero negativo. Por favor intentalo de nuevo')
#     iteador = 0
#     intentos = 1
#     while num < iteador and intentos != 3:
#         num = int(input('Escriba un numero para calcular el Fibonacci: '))
#         intentos += 1
#     print('\nLo siento, ingresaste tres veces numeros negativos')
#     print('-----------------FIN DEL PROGRAMA-----------------')
# else:
#     posicion_n = 0
#     if num == 0:
#         print(f'Escribiste el numero {num} y su Fibonacci es 0')
#     elif num == 1:
#         print(f'Escribiste el numero {num} y su Fibonacci es 1')
#     elif num > 1:
#         posicion0 = 0
#         posicion1 = 1
#         for i in range(num):
#             posicion_n = posicion0 + posicion1
#             posicion1 = posicion0
#             posicion0 = posicion_n
#         print(f'Escribiste el numero {num} y su Fibonacci es {posicion_n}')


# 04 - Escriba un programa que pida dos números enteros y escriba qué números son pares
# y cuáles impares desde el primero hasta el segundo.

# num1 = int(input('Ingresa un numero: '))
# num2 = int(input('Ingresa otro numero: '))
# num_pares = ''
# num_impares = ''
# corrida = 0
# if num1 > num2:
#     corrida = -1
#     num2 += -2
# else:
#     corrida = 1
# for i in range(num1,num2+1,corrida):
#     num = i % 2
#     if num == 0:
#         num_pares += f'{i} '
#     elif num != 0:
#         num_impares += "{} ".format(i)
# print('En el rango [{},{}]. Encontramos los numeros pares {} y los numeros impares {}'.format(num1, num2, num_pares, num_impares))
# print(f'En el rango [{num1},{num2}]. Encontramos los numeros pares {num_pares} y los numeros impares {num_impares}')



# intentos = 1
# num1 = int(input('Ingresa un numero entero positivo: '))
# num2 = int(input('Ingresa otro numero entero positivo: '))
#
# while intentos != 3 and num1 <= 0 or num2 <= 0:
#     print('ERROR--------> ingresa numero enteros positivos')
#     num1 = int(input('Ingresa un numero entero positivo: '))
#     num2 = int(input('Ingresa otro numero entero positivo: '))
#     intentos += 1
# else:
#     if num1 > 0 and num2 > 0:
#         par_num1 = num1 % 2
#         par_num2 = num2 % 2
#         if par_num1 == 0 and par_num2 == 0:
#             print(f'\nEl Primer numero que ingresaste {num1} es par\nEl Segundo numero que ingresaste {num2} es par')
#         elif par_num1 != 0 and par_num2 != 0:
#             print(f'\nEl Primer numero que ingresaste {num1} es impar\nEl Segundo numero que ingresaste {num2} es impar')
#         elif par_num1 == 0 and par_num2 != 0:
#             print(f'\nEl Primer numero que ingresaste {num1} es par\nEl Segundo numero que ingresaste {num2} es impar')
#         elif par_num1 != 0 and par_num2 == 0:
#             print(f'\nEl Primer numero que ingresaste {num1} es impar\nEl Segundo numero que ingresaste {num2} es par')
#     else:
#         print('\nIngresaaste solo numeros negativos. ejecuta de nuevo el programa')

# intentos = 1
# num1 = int(input('Ingresa un numero entero positivo: '))
# num2 = int(input('Ingresa otro numero entero positivo: '))
#
# while intentos != 3 and num1 <= 0 or num2 <= 0:
#     print('ERROR--------> ingresa numero enteros positivos')
#     num1 = int(input('Ingresa un numero entero positivo: '))
#     num2 = int(input('Ingresa otro numero entero positivo: '))
#     intentos += 1
# else:
#     if num1 > 0 and num2 > 0:
#         n_pares = ''
#         n_impares = ''
#         for i in range(num1,num2+1):
#             pares = i % 2
#             if pares == 0:
#                 n_pares += f"{i} "
#             else:
#                 n_impares += f"{i} "
#         print(f'Los numeros pares encontrados son: {n_pares} y los numeros impares son: {n_impares}')
#     else:
#         print('\nIngresaaste solo numeros negativos. ejecuta de nuevo el programa')


# 05 - Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

# num = int(input('Ingresa un numero entero mayor que cero: '))
# if num > 0:
#     divisores = ''
#     for i in range(num,0,-1):
#         divisor = num % i
#         if divisor == 0:
#             num_div = int(num / i)
#             divisores += f"{num_div} "
#     print(f'Los divisores de {num} son: {divisores}')


# 06 - Escriba un programa que pregunte cuántos números se van a introducir, pida esos números,
# y muestre un mensaje cada vez que un número no sea mayor que el primero.

# numIngresar = 0
# intentos = 0
# while intentos !=3 and numIngresar <= 0:
#     numIngresar = int(input('Cuantos numeros vas a querer ingresar: '))
#     intentos += 1
# if numIngresar > 0:
#     for i in range(1, (numIngresar + 1)):
#         numFirst = int(input('Ingresa un numero: '))
#         numNext = int(input('Ingresa otro numero: '))
#         if numNext > numFirst:
#             print(f'Numero {numNext} es Mayor que {numFirst}')
#         elif numFirst > numNext:
#             print(f'Numero {numFirst} es Mayor que {numNext}')


# numIngresar = 0
# intentos = 0
# while intentos !=3 and numIngresar <= 0:
#     numIngresar = int(input('Cuantos numeros vas a querer ingresar: '))
#     intentos += 1
# if numIngresar > 0:
#     numFirst = int(input('Ingresa un numero: '))
#     for i in range(1, (numIngresar + 1)):
#         numNext = int(input('Ingresa otro numero: '))
#         if numNext > numFirst:
#             print(f'Numero {numNext} es Mayor que {numFirst}')

# numIngresar = 0
# intentos = 0
# while intentos !=3 and numIngresar <= 0:
#     numIngresar = int(input('Cuantos numeros vas a querer ingresar: '))
#     intentos += 1
# if numIngresar > 0:
#     for i in range(1, (numIngresar + 1)):
#         numFirst = int(input('Ingresa un numero: '))
#         numNext = int(input('Ingresa otro numero: '))
#         if numNext > numFirst:
#             print(f'Numero {numNext} es Mayor que {numFirst}')


# 07 - Escriba un programa que pregunte cuántos números se van a introducir,
# pida esos números y escriba cuántos negativos ha introducido.

# numIngresar = 0
# intentos = 0
# while intentos !=3 and numIngresar <= 0:
#     numIngresar = int(input('Cuantos numeros vas a ingresar: '))
#     intentos += 1
# num = 0
# contador = 0
# negativos = ''
# for i in range(numIngresar):
#     num = int(input('Ingresa un numero negativo o positivo por favor: '))
#     if num < 0:
#         contador += 1
#         negativos += f"{num} "
# if num > 0:
#     print('\nNo escribiste numeros negativos')
# else:
#     print(f'\nLos numeros negativos que escribiste son: {negativos} y en total fueron {contador} numeros negativos')
#     print('\nFin del programa. Muchas gracias')


# 8 - Escriba un programa que pregunte cuántos números se van a introducir, pida esos números,
# y diga al final cuántos han sido pares y cuántos impares.

# numIngresar = 0
# intentos = 0
# while intentos !=3 and numIngresar <= 0:
#     numIngresar = int(input('Cuantos numeros vas a ingresar: '))
#     intentos += 1
# if numIngresar > 0:
#     numPares = ''
#     numImpares= ''
#     contadorPares = 0
#     contadorImpares = 0
#     for i in range(numIngresar):
#         num = int(input('Ingresa un numero: '))
#         par = num % 2
#         if par == 0:
#             numPares += f"{num } "
#             contadorPares += 1
#         else:
#             numImpares += f"{num } "
#             contadorImpares += 1
# print(f'\nLos Numero pares fueron: {numPares} con un total de {contadorPares}\n'
#       f'Los Numero impares fueron: {numImpares} con un total de {contadorImpares}')

# 09 - Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
# y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la
# inversión.

# cantidadInversion = float(input('Ingresa el monto a invertir: '))
# interesAnual = float(input('Ingresa el porcentaje de interes anual: '))
# anos = int(input('Ingresa los años: '))
# for i in range(anos):
#     cantidadInversion *= 1 + (interesAnual / 100)
#     #print('El capital despues de', i+1, 'años: ', str(round(cantidadInversion,2)))
#     print('El capital despues de {} años: {}'.format(i+1,str(round(cantidadInversion,2))))


# 10 - Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una
# las letras de la palabra introducida empezando por la última.

# palabra = input('Escribe una palabra por favor: ')
# salida = ''
# for i in palabra:
#     salida = f"{i + salida}"
#     print(salida)
# for i in salida:
#     print(i)


# 11 - Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase.

# frase = input('Escribe una frase por favor: ')
# letra = input('Ahora especifica una letra para encontrarla: ')
# contador = 0
# for i in frase:
#     if letra == i:
#         contador += 1
# print(f'La letra {letra} se encuentra {contador} veces')
# print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))


# 12 - Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales
# que aparecen en esa frase (sin repetirlas).

# frase = input('Escribe una frase por favor: ')
# vocales = 'aeiou'
# acumulador = ''
#
# for i in vocales:
#     if i in frase:
#         acumulador += f"{i} "
# print(f'La vocales encontradas en la frase son: {acumulador}')


# CLASE 25/05/2021-----------------------------------------------------------------------------------------------------

## 01 - Elaborar un algoritmo que permita mostrar el sueldo promedio de un grupo de empleados.

# salario = 0
# sumaSalarios = 0
# empleados = int(input('Ingresa el numero de empleados: '))
# for i in range(1,empleados+1):
#     salario = int(input(f'Ingresa el salario del empleado {i}: '))
#     sumaSalarios += salario
# promedio = sumaSalarios / empleados
# print(f'El sueldo promedio de {empleados} empleados es {promedio}')



## 02 - Elaborar un algoritmo que solicite la edad de 10 personas, y que muestre cuantos son mayores y cuantos
## menores.

# cuentaMayores = 0
# cuentaMenores = 0
# for i in range(1,11):
#     edad = int(input('Ingresa la edad correspondiente a la persona {}: '.format(i)))
#     if edad >= 18:
#         cuentaMayores += 1
#     else:
#         cuentaMenores += 1
# print()
# print('Tenemos {} personas mayores y {} personas menores.'.format(cuentaMayores, cuentaMenores))



## 04 - Elabore un algoritmo que solicite ingresar letras hasta que ingresen una vocal.

# estado = True
# while estado:
#     letra = input('Ingresa una letra por favor: ')
#     ingreso = letra.upper()
#     if ingreso == 'A' or ingreso == 'E' or ingreso == 'I' or ingreso == 'O' or ingreso == 'U':
#         estado = False



## 05 - Elaborar un programa que permita ingresar una frase y contar la cantidad de vocales, por separado.
## es decir cuantas vocales A,E,I,O,U  se ingresaron en la frase.

# frase = input('Escribe una frase por favor: ')
# vocales = 'aeiou'
# contA = 0
# contE = 0
# contI = 0
# contO = 0
# contU = 0
# frase = frase.upper()
# vocales = vocales.upper()
# for i in frase:
#     if i in vocales:
#         if i == 'A':
#             contA += 1
#         elif i == 'E':
#             contE += 1
#         elif i == 'I':
#             contI += 1
#         elif i == 'O':
#             contO += 1
#         elif i == 'U':
#             contU += 1
# print(f'Encontramos la vocal A: {contA} veces')
# print(f'Encontramos la vocal E: {contE} veces')
# print(f'Encontramos la vocal I: {contI} veces')
# print(f'Encontramos la vocal O: {contO} veces')
# print(f'Encontramos la vocal U: {contU} veces')

## 06 - Elaborar un programa para obtener el resultado del escrutinio en las elecciones del delegado del colegio
## cosiderar que hay 20 electores y se han presentado 3 candidatos, todos votaron, el algoritmo debe
## declarar el ganador por mayoria simple.

# candidatos = 3
# electores = 20
# cont1 = 0
# cont2 = 0
# cont3 = 0
# contx = 0
#
# for i in range(electores):
#     voto = int(input('Escriba es numero del cadidato que desea votar: '))
#     if voto == 1:
#         cont1 += 1
#     elif voto == 2:
#         cont2 += 1
#     elif voto == 3:
#         cont3 += 1
#     else:
#         print("No existe ese candidato")
#         contx += 1
# if cont1 > cont2 and cont1 > cont3:
#     print('El ganador es el candidato 1 con {} votos'.format(cont1))
# elif cont2 > cont1 and cont2 > cont3:
#     print('El ganador es el candidato 2 con {} votos'.format(cont2))
# elif cont2 > cont1 and cont2 > cont3:
#     print('El ganador es el candidato 3 con {} votos'.format(cont3))
# else:
#     print('No existe ganador. Fueron {} votos anulados o erroneos'.format(contx))
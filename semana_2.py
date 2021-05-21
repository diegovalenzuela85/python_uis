'''
print('Hola... a continuación ingresa tu salario')
salario = int(input())
alimentacion = salario * 0.4
servicios = salario * 0.2
cine = salario * 0.1

print("Tu sueldo es de: ",salario)
print("Tienes destinado para Alimentos un valor de:", alimentacion)
print("Tienes destinado para Servicios un valor de:", servicios)
print("Tienes destinado para Cine un valor de:", cine)
print("Y te sobra", salario - alimentacion - servicios - cine," para el arriendo de tu vivienda")



## Sumar dos números enteros y que me arroje el resultado
num_1 = int(input("\n"))
num_2 = int(input())
suma = num_1 + num_2
print(suma)



## EJER 1 Calcular La distancia recorrida (m) por un movil
## que tiene velocidad constante (m/s) durante un tiempo T
## (sg), conciderar que es MRU (Movimiento rectilineo Uniforme)

velocidad = float(input('Ingrese la velocidad constante\n'))
tiempo = int(input('Ingrese el tiempo\n'))
distancia = velocidad * tiempo
print('La distancia es: ', distancia, 'm')



## Se necesita obtener un promedio simple de un estudiante a partir de sus tres notas parciales

nota_1 = float(input('Ingrese nota 1: '))
if nota_1 <= 5:
    nota_1 = nota_1
else:
    print('Nota 1 no es valida, sobrepasa el rango correcto 0 - 5', 'ingresaste:', nota_1)
    nota_1 = float(input('Ingrese nota 1: '))

nota_2 = float(input('Ingrese nota 2: '))
if nota_2 <= 5:
    nota_2 = nota_2
else:
    print('Nota 2 no es valida, sobrepasa el rango correcto 0 - 5', 'ingresaste:', nota_2)
    nota_2 = float(input('Ingrese nota 2: '))

nota_3 = float(input('Ingrese nota 3: '))
if nota_3 <= 5:
    nota_3 = nota_3
else:
    print('Nota 3 no es valida, sobrepasa el rango correcto 0 - 5', 'ingresaste:', nota_3)
    nota_3 = float(input('Ingrese nota 3: '))

promedio = (nota_1 + nota_2 + nota_3) / 3
print('Su promedio es: ', promedio)



## Elabore un algoritmo que solicite rtas correctas, incorrectas y en blanco. Muestre su puntaje
## final considerando Por cada rta correcta tendra 4puntos, rta incorrecta -1punto, en blanco 0.

correctas = int(input('Ingrese las respuestas correctas: '))
incorrectas = int(input('Ingrese las respuestas incorrectas: '))
blanco = int(input('Ingrese las respuestas en blanco: '))

puntaje = (correctas * 4) + (incorrectas * -1) + (blanco * 0)
print('Su puntaje es: ', puntaje)



## Ingresar # partidos ganados, perdidos y empacados.
## Mostrar punje total de acuerdo. Partido ganado obtendra 3 puntos
## Empate 1 punto y perdido 0 puntos
pGanados = int(input('Ingrese numero partidos ganados: '))
pEmpatado = int(input('Ingrese numero partidos empatados: '))
pPerdidos = int(input('Ingrese numero partidos perdidos: '))
puntaje = (pGanados * 3) + (pEmpatado * 1)
print('El puntaje obtenido es: ', puntaje)



## Elaborar la planilla de un empleado, se disone de horas laboradas en el mes
## y la tarifa por hora
horas_laboradas = float(input('Ingrese la cantidad de horas laboradas: '))
tarifa_hora = float(input('Ingrese la tarifa de horas laboradas: '))
salario = horas_laboradas * tarifa_hora
print('Su salario es de: ', salario)



horas_laboradas = float(input('Ingrese la cantidad de horas laboradas: '))
tarifa_hora = float(input('Ingrese la tarifa de horas laboradas: '))
salario = horas_laboradas * tarifa_hora

descuento_salud_empleado = salario * 0.04
descuento_pension_empleado = salario * 0.04

totalDescontadoEmpleado = descuento_salud_empleado + descuento_pension_empleado
salario_neto = salario - totalDescontadoEmpleado

descuento_salud_empresa = salario * 0.085
descuento_pension_empresa = salario * 0.08

total_salud = descuento_salud_empresa + descuento_salud_empleado
total_pensiones = descuento_pension_empresa + descuento_pension_empleado

print('El valor del salario Bruto es de: ', salario)
print('El total que se debe pagar por salud ', total_salud, 'y pensiones ', total_pensiones)
print('Los descuentos para el empleado son: ', 'En salud es ', descuento_salud_empleado, 'En pensiones es ', descuento_pension_empleado, 'Con un total descontado de ', totalDescontadoEmpleado)
print('La empresa paga: ', 'En salud ', descuento_salud_empresa, 'En pensiones ', descuento_pension_empleado)
print('El salario neto es de: ', salario_neto)


num = int(input('Introducta un numero: '))
if num == 100:
    print('Usted escribio: ', num)
else:
    print('No escribiste en numero indicado')


## Identificar si el numero ingresado es positivo
num = float(input('Ingresa un numero: '))
if num > 0:
    print('El numero ingresado es positivo:', num)
else:
    print('El numero ingresado es negativo')


## Ingresar un numero e indentificar si es mayor o igual a 1000
num = float(input('Ingresar un numero: '))
if num >= 1000:
    print('El numero es mayor o igual a 1000')


## Ingresar un nuemro e identificar si es par, no tener en cuenta el cero
num = float(input('Ingrese un numero: '))
identificacion = num % 2
if identificacion ==0:
    print('El nuemero ingrsado en PAR', num)

num = float(input('Ingrese un numero: '))
if num % 2 == 0:
    print('El nuemero ingrsado en PAR', num)


num = float(input('Ingrese un numero: '))
if num % 2 != 0:
    print('El numero ingrsado en IMPAR', num)

## Ingresar un numero e identificar si es menor de 500 , no tener en cuenta el cero
num = float(input('Ingrese un numero: '))
if num < 500 and num != 0:
    print('El numero ingresado es menor que 500')

## Ingresar un numero e identificar se es mayor a 100, no tener en cuenta el cero
num = float(input('Ingrese un numero: '))
if num > 100 and num != 0:
    print('El numero ingresado es menor que 100')

## ingrese un numero e identificar si es mayor o igual a -200 y menor a 200
num = float(input('Ingrese un numero: '))
if num >= -200 and num < 200:
    print('El numero ingresado esta en el rango de [-200,200]')


## Ingresar un nombre en mayuscula e idetificar si esta entre ('MARIA','PEDRO','JOSE','JESUS','LUIS')
nombre = input('Ingresa un Nombre en MAYUSCULA: ')
if nombre == 'MARIA' or nombre == 'PEDRO' or nombre == 'JOSE' or nombre == 'JESUS' or nombre == 'LUIS':
    print('Tu nombre es: ', nombre)

nombre = input('Ingresa un Nombre en MAYUSCULA: ')
if nombre != 'MARIA' and nombre != 'PEDRO' and nombre != 'JOSE' and nombre != 'JESUS' and nombre != 'LUIS':
    print('Tu nombre es: ', nombre)

nombre = input('Ingresa un Nombre en MAYUSCULA: ')
if not(nombre == 'MARIA' or nombre == 'PEDRO' or nombre == 'JOSE' or nombre == 'JESUS' or nombre == 'LUIS'):
    print('Tu nombre es: ', nombre)


## Ingresar dos nombres en mayuscula e identificar si el primer nombre es "JOSE" y el segundo nombre es ""LUIS
nombre1 = input('Ingresa un Nombre en MAYUSCULA: ')
nombre2 = input('Ingresa un Nombre en MAYUSCULA: ')
if nombre1 == 'JOSE' and nombre2 == 'LUIS':
    print('Tu primer nombre es: ', nombre1, 'y tu segundo nombre es: ', nombre2)


num = int(input('Introducta un numero: '))
if num == 100:
    print('Usted escribio: ', num)
else:
    print('Usted escribio: ', num,'Distinto a 100')


## Ingrese dos numeros enteros y calcule su división, Escribiendo si la división es exacta o no
num1 = int(input('Introducta un numero: '))
num2 = int(input('Introducta un numero: '))
operacion = num1 / num2
division = num1 % num2
if division == 0:
    operacion = int(operacion)
    print('La división es exacta y su resultado es: ', operacion)
else:
    print('La división NO es exacta y su resultado es:', operacion)


# Solicitar dos numeros y mostrar si son iguales o no
num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese un numero: '))
if num1 == num2:
    print(f"El prrimer numero que ingresaste {num1} es igual al segundo numero ingresado {num2}")
else:
    print('Los numeros que ingresaste son distintos')


# Solicitar edad de dos hermanos y  muestre un mensaje indicando la edad del mayor y cuantos años de diferencia tiene con el menor
edad1 = int(input('Edad hermano uno: '))
edad2 = int(input('Edad hermano dos: '))

if 0<edad1<100 and 0<edad2<100:
    if edad1 > edad2:
        diferecia = edad1 - edad2
        print(f'La primera edad ingresada es mayor que la segunda edad ingresada, La diferencia de edad es de {diferecia}años')
    elif edad2 > edad1:
        diferecia = edad2 - edad1
        print(f'La segunda edad ingresada es mayor que la primera edad ingresada, La diferencia de edad es de {diferecia}años')
    elif edad1 == edad2:
        diferecia = edad1 - edad2
        print(f'La primera edad ingresada es igual que la segunda edad ingresada, La diferencia de edad es de {diferecia}años')
else:
    print('La edad no es valida, por favor ingresa un numero Valido')

# Solicitar una letra y decir si es vocal o consonante
letra = input('Escriba una LETRA por favor: ')
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print(f'La letra que ingresaste es {letra}, por lo tanto es una vocal')
elif letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print(f'La letra que ingresaste es {letra}, por lo tanto es una vocal')
else:
    print(f'La letra que ingresaste es {letra}, por lo tanto es una consonante')

# Leer dos valores distintos, determinar cual de los dos valores es mayor y escribirlo
valor1 = float(input('Por favor escriba un valor: '))
valor2 = float(input('Por favor escriba un valor: '))
if valor1 > valor2:
    print(f'El primer valor ingresado es {valor1} y es mayor que {valor2}')
elif valor2 > valor1:
    print(f'El segundo valor ingresado es {valor2} y es mayor que {valor1}')
elif valor1 == valor2:
    print(f'El primer valor ingresado es: {valor2} y  el segundo valor ingresado es: {valor1}. Son valores iguales')


# Pedir unidades producidas por semana (lunes-sabado). Elaborar un algoritmo que muestre si el operario recibira incentivos o no sabiendo que la producción minima es 100 unidades
lunes = int(input('Ingresa las unidadades producidas el lunes: '))
martes = int(input('Ingresa las unidadades producidas el martes: '))
miercoles = int(input('Ingresa las unidadades producidas el miercoles: '))
jueves = int(input('Ingresa las unidadades producidas el jueves: '))
viernes = int(input('Ingresa las unidadades producidas el viernes: '))
sabado = int(input('Ingresa las unidadades producidas el sabado: '))

if lunes > 100:
    print(f'La producción del lunes es de: {lunes}unidades. Por lo tanto tienes bonificación OK')
else:
    print(f'Lo siento..., Para el dia lunes NO tienes bonificación por que la producción es de {lunes}unidades, siendo menor a la cantidad minima 100 unidades')
if martes > 100:
    print(f'La producción del martes es de: {martes}unidades. Por lo tanto tienes bonificación OK')
else:
    print(f'Lo siento..., Para el dia martes NO tienes bonificación por que la producción es de {martes}unidades, siendo menor a la cantidad minima 100 unidades')
if miercoles > 100:
    print(f'La producción del miercoles es de: {miercoles}unidades. Por lo tanto tienes bonificación OK')
else:
    print(f'Lo siento..., Para el dia miercoles NO tienes bonificación por que la producción es de {miercoles}unidades, siendo menor a la cantidad minima 100 unidades')
if jueves > 100:
    print(f'La producción del jueves es de: {jueves}unidades. Por lo tanto tienes bonificación OK')
else:
    print(f'Lo siento..., Para el dia jueves NO tienes bonificación por que la producción es de {jueves}unidades, siendo menor a la cantidad minima 100 unidades')
if viernes > 100:
    print(f'La producción del viernes es de: {viernes}unidades. Por lo tanto tienes bonificación OK')
else:
    print(f'Lo siento..., Para el dia viernes NO tienes bonificación por que la producción es de {viernes}unidades, siendo menor a la cantidad minima 100 unidades')
if sabado > 100:
    print(f'La producción del sabado es de: {sabado}unidades. Por lo tanto tienes bonificación OK')
else:
    print(f'Lo siento..., Para el dia sabado NO tienes bonificación por que la producción es de {sabado}unidades, siendo menor a la cantidad minima 100 unidades')


# Obtener dos numeros y ordenarlos de menor a mayor si es el caso
num1 = float(input('Ingresa un numero por favor: '))
num2 = float(input('Ingresa un numero por favor: '))
if num1 < num2:
    print(f'{num1}"," {num2}')
elif num2 < num1:
    print(num2, ",", num1)
else:
    print('Lo siento, los numeros son iguales, no existe orden')


# pedir numero y verificar que sea 100, si es asi mostrar en pantalla si no cumple decir si es mayor o menor
num = float(input('Escriba un numero: '))
if num == 100:
    print(f'El numero ingresado es: {num}')
elif num < 100:
    print(f'En numero ingresado es {num} menor que 100')
else:
    print(f'En numero ingresado es {num} mayor que 100')


# identificar el rango en que es un numero solicitado en pantalla
num = float(input('Ingrese un numero: '))
if num < 0:
    print(f'Tu numero ingresado es {num} y es menor a cero')
elif 0 <= num < 10:
    print(f'Tu numero ingresado es {num} y esta en el rango de [0 , 10]')
elif 11 <= num < 50:
    print(f'Tu numero ingresado es {num} y esta en el rango de [11 , 50]')
elif 51 <= num < 100:
    print(f'Tu numero ingresado es {num} y esta en el rango de [51 , 100]')
else:
    print(f'Tu numero ingresado es {num} y es mayor que 100')


# Ingresar dos numeros y mostrar cual de los dos es menor. Considerar nuemros iguales
num1 = int(input('Ingresa un numero por favor: '))
num2 = int(input('Ingresa un numero por favor: '))
if num1 < num2:
    print(f'{num1} "es menor que" {num2}')
elif num2 < num1:
    print(num1, "es mayor que", num2)
else:
    print('los numeros son iguales')


# Ingresar tres numeros diferentes entre si, determinar el nuemro mayor de los tres
num1 = int(input('Ingresa un numero por favor: '))
num2 = int(input('Ingresa un numero por favor: '))
num3 = int(input('Ingresa un numero por favor: '))

if num1 != num2 and num1 != num3 and num2 != num3:
    if num1 > num2 and num1 > num3:
        print(f'El numero mayor es: {num1}')
    elif num2 > num1 and num2 > num3:
        print(f'El numero mayor es: {num2}')
    elif num3 > num1 and num3 > num2:
        print(f'El numero mayor es: {num3}')


num1 = int(input('Ingresa un numero por favor: '))
num2 = int(input('Ingresa un numero por favor: '))
num3 = int(input('Ingresa un numero por favor: '))

if num1 != num2 and num1 != num3 and num2 != num3:
    if num1 > num2 and num1 > num3:
        print(f'El numero mayor es: {num1}')
    elif num2 > num3:
        print(f'El numero mayor es: {num2}')
    else:
        print(f'El numero mayor es: {num3}')


# Solicitar 3 numeros y pueden ser repetidos y determinar el numero mayor
num1 = int(input('Ingresa un numero por favor: '))
num2 = int(input('Ingresa un numero por favor: '))
num3 = int(input('Ingresa un numero por favor: '))
if num1 != num2 and num1 != num3 and num2 != num3:
    if num1 > num2 and num1 > num3:
        print(f'El numero mayor es: {num1}')
    elif num2 > num3:
        print(f'El numero mayor es: {num2}')
    else:
        print(f'El numero mayor es: {num3}')
elif num1 == num2:
    if num1 > num3:
        print(f'Los numeros mayores son: {num1} y {num2}')
    else:
        print(f'El numero mayor es: {num3}')
elif num2 == num3:
    if num2 > num1:
        print(f'Los numeros mayores son: {num2} y {num3}')
    else:
        print(f'El numero mayor es: {num1}')
elif num1 == num3:
    if num1 > num2:
        print(f'Los numeros mayores son: {num1} y {num3}')
    else:
        print(f'El numero mayor es: {num2}')
else:
    print('Todos los numeros son repetidos')


num1 = int(input('Ingresa un numero por favor: '))
num2 = int(input('Ingresa un numero por favor: '))
num3 = int(input('Ingresa un numero por favor: '))

if num1 != num2 and num1 != num3 and num2 != num3:
    if num1 > num2 and num1 > num3:
        print(f'El numero mayor es: {num1}')
    elif num2 > num3:
        print(f'El numero mayor es: {num2}')
    else:
        print(f'El numero mayor es: {num3}')
else:
    if num1 == num2 and num2 == num3:
        print('Todos los numeros son iguales')
    elif num1 == num2 and num2 > num3:
        print(f'{num1} y {num2} son mayores ')
    elif num1 == num3 and num1 > num2:
        print(f'{num1} y {num3} son mayores ')
    else:
        print(f'{num2} y {num3} son mayores ')


# Elaborar un algoritmo que sirva para identificar el tipo de triangulo conociendo la longitud de ssu lados - Equilatero, isoceles - escaleno
ladoA = int(input('Ingresa el lado A por favor: '))
ladoB = int(input('Ingresa un lado B por favor: '))
ladoC = int(input('Ingresa un lado C por favor: '))
if ladoA == ladoB and ladoB == ladoC:
    print('El triangulo ingresado es equilatero')
elif ladoA != ladoB and ladoB != ladoC and ladoA != ladoC:
    print('El triangulo ingresado es escaleno')
else:
    print('El triangulo ingresado es isoceles')


# entrar un numero entero de (1 a 10), Mostrar equivalente en romano
num = int(input('Por favor escriba un numero de 1 a 10: '))
if num == 1:
    print('Su numero Romano es: I')
elif num == 2:
    print('Su numero Romano es: II')
elif num == 3:
    print('Su numero Romano es: III')
elif num == 4:
    print('Su numero Romano es: IV')
elif num == 5:
    print('Su numero Romano es: V')
elif num == 6:
    print('Su numero Romano es: VI')
elif num == 7:
    print('Su numero Romano es: VII')
elif num == 8:
    print('Su numero Romano es: VIII')
elif num == 9:
    print('Su numero Romano es: IX')
elif num == 10:
    print('Su numero Romano es: X')
else:
    print('Su numero no esta dentro del rango solicitado')



#  Ingresar monto ventas durante un mes y luego calcular bonificación
monto_ventas = float(input('Ingresar monto de ventas mensuales: '))
if 0 <= monto_ventas < 1000000:
    print(f'Su bonificación es de {monto_ventas * 0} Pesos')
elif 1000000 <= monto_ventas < 5000000:
    print(f'Su bonificación es de {monto_ventas * 0.03} Pesos')
elif 5000000 <= monto_ventas < 20000000:
    print(f'Su bonificación es de {monto_ventas * 0.05} Pesos')
elif monto_ventas >= 20000000:
    print(f'Su bonificación es de {monto_ventas * 0.08} Pesos')


# Solicitar numero entero y mostrar vocal correspondiente A=1
num = int(input('Ingrese un numero de 1 a 5: '))
if 1 <= num <= 5:
    if num == 1:
        print('A')
    elif num == 2:
        print('E')
    elif num == 3:
        print('I')
    elif num == 4:
        print('O')
    else:
        print('U')
else:
    print('El numero ingresado no esta en el rango solicitado')


# Ingresar tres valores distintos A,B,C almacenarlos en las varibles, imprimir cual es el mayor y cual es el menor, Constatar que los tres valores sean diferentes, Presente un mensaje de alerta en caso de que se detecte la introducción de valores iguales
a = int(input('Ingrese un numero A: '))
b = int(input('Ingrese un numero B: '))
c = int(input('Ingrese un numero C: '))
if a != b and b != c and a != c:
    if a > b and b > c and a > c:
        print(f'el numero mayor es {a} y el numero menor es {c}')
    elif b > a and a > c and b > c:
        print(f'el numero mayor es {b} y el numero menor es {c}')
    elif c > a and b > a and c > b:
        print(f'el numero mayor es {c} y el numero menor es {a}')
    elif b > c and c > a and b > a:
        print(f'el numero mayor es {b} y el numero menor es {a}')
    elif a > c and c > b and a > b:
        print(f'el numero mayor es {a} y el numero menor es {b}')
    elif c > b and a > b and c > a:
        print(f'el numero mayor es {c} y el numero menor es {b}')
else:
    print('Error.... No se pueden envia numeros iguales')

'''
# Obtener cantidad de helados y si desea topping, al final debe informar valor a pagar
oreo = int(input('Ingresa la cantidad helados con oreo: '))
kikkat = int(input('Ingresa la cantidad helados con kitkat: '))
brownie = int(input('Ingresa la cantidad helados con brownie: '))
lacasitos = int(input('Ingresa la cantidad helados con lacasitos: '))
heladosSin = int(input('Ingresa la cantidad de helados sin topping: '))
precioFijo = float(1900)
if oreo >= 0 and kikkat >= 0 and brownie>= 0 and lacasitos >= 0 and heladosSin >= 0:
    if oreo >= 0:
        oTotal = (precioFijo + 1000) * oreo
        print(f'{oreo} helados con topping de oreo por un valor de {oTotal}')
        if kikkat >= 0:
            kTotal = (precioFijo + 1500) * kikkat
            print(f'{kikkat} helados con topping de kikkat por un valor de {kTotal}')
            if brownie >= 0:
                bTotal = (precioFijo + 750) * brownie
                print(f'{brownie} helados con topping de Brownie por un valor de {bTotal}')
                if lacasitos >= 0:
                    lTotal = (precioFijo + 1000) * lacasitos
                    print(f'{lacasitos} helados con topping de lacasitos por un valor de {lTotal}')
                    if heladosSin >= 0:
                        hTotal = precioFijo * heladosSin
                        print(f'{heladosSin} helados sin topping por un valor de {hTotal}')
                        total = oTotal + kTotal + bTotal + lTotal + hTotal
                        print(f'Por un total de {total}')
else:
    print('Cantidad no valida')
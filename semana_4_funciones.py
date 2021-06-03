'''
        EJERCICIO str()

        Diseñar el algoritmo correspondiente a un programa que al introducir una cantidad de dinero expresado
        en pesos nos indique cuántos billetes y monedas se puede tener como mínimo (Billetes de 1000, 2000, 5000,
        10000, 20000 y 50000, monedas de 20, 50, 100, 200 y 500).
'''


# monto = int(input('Ingresa el monto a calcular: '))
# d_billetes = [50000,20000,10000,5000,2000,1000]
# d_monedas = [500,200,100,50,20]
# billetes = ""
# monedas = ""
#
# for b in d_billetes:
#     billete = int(monto // b)
#     if billete > 0:
#         #billetes += f"({b},{billete}) "
#         #billetes += "(" + str(b) + "," + str(billete) + ")"
#         #billetes += "(" + "Necesito " + str(billete) + " Billetes de " + str(b) + " pesos\n"
#         billetes += f"Necesito {billete} Billetes de {b} pesos\n"
#         monto -= (b * billete)
# for m in d_monedas:
#     moneda = int(monto // m)
#     if moneda > 0:
#         #monedas += f"({m},{moneda}) "
#         #monedas += "(" + str(m) + "," + str(moneda) + ")"
#         monedas += "Necesito " + str(moneda) + " Monedas de " + str(m) + " pesos\n"
#         monto -= (m * moneda)
#
# print(f'{billetes}{monedas}')

'''
    --------------------------------------- FUNCIONES PROPIAS --------------------------------------------
    
    Variables locales: 
    Si no se han declarado como globales o no locales, las variables a las que se asigna valor en una
    función se consideran variables locales, es decir, sólo existen en la propia función, incluso cuando en
    el programa exista una variable con el mismo nombre, como muestra el siguiente ejemplo:
'''
# def subrutina():
#     a = 2
#     print(a)
#     return
# a = 5
# subrutina()
# print(a)


'''
    Las variables locales sólo existen en la propia función y no son accesibles
    desde niveles superiores, como puede verse en el siguiente ejemplo:
'''

# def subrutina():
#     a = 2
#     print(a)
#     return
# subrutina()
# print(a)

'''
    Si en el interior de una función se asigna valor a una variable que no se ha declarado como global o
    no local, esa variable es local a todos los efectos. Por ello el siguiente programa da error:
'''

# def subrutina():
#     print(a)
#     a = 2
#     print(a)
#     return
# a = 5
# subrutina()
# print(a)

'''
    Variables libres globales o no locales:
    Si a una variable no se le asigna valor en una función, Python la considera libre y busca su valor en los
    niveles superiores de esa función, empezando por el inmediatamente superior y continuando hasta el programa
    principal. Si a la variable se le asigna valor en algún nivel intermedio la variable se considera no local
    y si se le asigna en el programa principal la variable se considera global, como muestran los siguientes ejemplos:
    
    En el ejemplo siguiente, la variable libre "a" de la función subrutina() se considera global porque obtiene
    su valor del programa principal:
'''

# def subrutina():
#     print(a)
#     return
# a = 5
# subrutina()
# print(a)

'''
    En el ejemplo siguiente, la variable libre "a" de la función sub_subrutina() se considera no local
    porque obtiene su valor de una función intermedia:
'''

# def subrutina():
#     def sub_subrutina():
#         print(a)
#         return
#     a = 3
#     sub_subrutina()
#     print(a)
#     return
# a = 4
# subrutina()
# print(a)

'''
    Si a una variable que Python considera libre (porque no se le asigna valor en la función) tampoco se
    le asigna valor en niveles superiores, Python dará un mensaje de error, como muestra el programa siguiente:
'''

# def subrutina():
#     print(a)
#     return
# subrutina()
# print(a)}

'''
    Variables declaradas global o nonlocal:
    Si queremos asignar valor a una variable en una subrutina, pero no queremos que Python la
    considere local, debemos declararla en la función como global o nonlocal, como muestran los
    ejemplos siguientes:
    
    En el ejemplo siguiente la variable se declara como global, para que su valor sea el del
    programa principal:
'''

# def subrutina():
#     global a
#     print(a)
#     a = 1
#     return
# a = 5
# subrutina()
# print(a)

'''
    En el ejemplo siguiente la variable se declara como nonlocal, para que su valor sea el de la función intermedia:
'''

# def subrutina():
#     def sub_subrutina():
#         nonlocal a
#         print(a)
#         a = 1
#         return
#     a = 3
#     sub_subrutina()
#     print(a)
#     return
# a = 4
# subrutina()
# print(a)

'''
    Si a una variable declarada global o nonlocal en una función no se le asigna valor en el nivel superior
    correspondiente, Python dará un error de sintaxis, como muestra el programa siguiente:
'''

# def subrutina():
#     def sub_subrutina():
#         nonlocal a
#         print(a)
#         a = 1
#         return
#     sub_subrutina()
#     print(a)
#     return
# a = 4
# subrutina()
# print(a)

'''
    Argumentos y devolución de valores:
    Las funciones en Python admiten argumentos en su llamada y permiten devolver valores. Estas 
    posibilidades permiten crear funciones más útiles y fácilmente reutilizables. En este apartado 
    se muestran estos conceptos mediante cuatro ejemplos. En ellos, no se pretende encontrar la
    mejor solución al problema planteado, sino simplemente introducir los conceptos de argumentos
    y devolución de valores.
    
    Aunque las funciones en Python pueden acceder a cualquier variable del programa declarándolas 
    como variables globales o no locales, se necesita saber el nombre de las variables, como muestra
    el ejemplo siguiente:    
'''

# def escribe_media():
#     media = (a + b) / 2
#     print(f"La media de {a} y {b} es: {media}")
#     return
# a = 3
# b = 5
# escribe_media()
# print("Programa terminado")
'''
 NOTA: El problema de una función de este tipo es que es muy difícil de reutilizar en otros programas o 
    incluso en el mismo programa, ya que sólo es capaz de hacer la media de las variables "a" y "b".
    Si en el programa no se utilizan esos nombres de variables, la función no funcionaría.
'''

'''
    Para evitar ese problema, las funciones admiten argumentos, es decir, permiten que se les envíen
    valores con los que trabajar. De esa manera, las funciones se pueden reutilizar más fácilmente,
    como muestra el ejemplo siguiente:
'''

# def escribe_media(x, y):
#     media = (x + y) / 2
#     print(f"La media de {x} y {y} es: {media}")
#     return
# a = 3
# b = 5
# escribe_media(a, b)
# print("Programa terminado")
'''
    NOTA: Pero esta función tiene todavía un inconveniente. Como las variables locales de una
    función son inaccesibles desde los niveles superiores, el programa principal no puede utilizar
    la variable "media" calculada por la función y tiene que ser la función la que escriba el valor.
    Pero eso complica la reutilización de la función, porque aunque es probable que en otro programa
    nos interese una función que calcule la media, es más difícil que nos interese que escriba el
    valor nada más calcularlo.
'''

'''
    Para evitar ese problema, las funciones pueden devolver valores, es decir, pueden enviar valores
    al programa o función de nivel superior. De esa manera, las funciones se pueden reutilizar más
    fácilmente, como muestra el ejemplo siguiente:
'''

# def calcula_media(x, y):
#     resultado = (x + y) / 2
#     return resultado
# a = 3
# b = 5
# media = calcula_media(a, b)
# print(f"La media de {a} y {b} es: {media}")
# print("Programa terminado")

'''
    Para evitar ese problema, las funciones pueden devolver valores, es decir, pueden enviar
    valores al programa o función de nivel superior. De esa manera, las funciones se pueden
    reutilizar más fácilmente, como muestra el ejemplo siguiente:
'''

# def calcula_media(x, y):
# #     resultado = (x + y) / 2
# #     return resultado
# # a = 3
# # b = 5
# # media = calcula_media(a, b)
# # print(f"La media de {a} y {b} es: {media}")
# # print("Programa terminado")
'''
    NOTA: Pero esta función tiene todavía un inconveniente y es que sólo calcula la media de
    dos valores. Sería más interesante que la función calculara la media de cualquier cantidad
    de valores.
'''

'''
    Para evitar ese problema, las funciones pueden admitir una cantidad indeterminada de valores, 
    como muestra el ejemplo siguiente:
'''

# def calcula_media(*args):
#     total = 0
#     for i in args:
#         total += i
#     resultado = total / len(args)
#     return resultado
# a, b, c = 3, 5, 10
# media = calcula_media(a, b, c)
# print(f"La media de {a}, {b} y {c} es: {media}")
# print("Programa terminado")

'''
    Las funciones pueden devolver varios valores simultáneamente, como muestra el siguiente ejemplo:
'''

# def calcula_media_desviacion(*args):
#     total = 0
#     for i in args:
#         total += i
#     media = total / len(args)
#     total = 0
#     for i in args:
#         total += (i - media) ** 2
#     desviacion = (total / len(args)) ** 0.5
#     return media, desviacion
# a, b, c, d = 3, 5, 10, 12
# media, desviacion_tipica = calcula_media_desviacion(a,
# b, c, d)
# print(f"Datos: {a} {b} {c} {d}")
# print(f"Media: {media}")
# print(f"Desviación típica: {desviacion_tipica}")
# print("Programa terminado")


'''
    Conflictos entre nombres de parámetros y nombre de variables globales:
    
    En Python no se producen conflictos entre los nombres de los parámetros y los nombres
    de las variables globales. Es decir, el nombre de un parámetro puede coincidir o no con el
    de una variable global, pero Python no los confunde: en el ámbito de la función el 
    parámetro hace siempre referencia al dato recibido y no a la variable global y los 
    programas producen el mismo resultado.
    
    Eso nos facilita reutilizar funciones en otros programas sin tener que preocuparnos por
    este detalle.
    
    Aunque, como siempre, dependiendo de si a la función se le envía como parámetro un
    objeto mutable o inmutable, la función podrá modificar o no al objeto. En los dos 
    siguientes ejemplos, el parámetro de la función ("b") se llama igual que una de las dos
    variables del programa principal. En los dos ejemplos se llama dos veces a la función, 
    enviando cada vez una de las dos variables ("a" y "b").
    
    
    Ejemplo de conflicto entre nombre de parámetro y nombre de variable global. Objeto mutable
    Como en este caso las variables son listas (objetos mutables), la función modifica la lista
    que se envía como argumento: primero se modifica la lista "a" y a continuación la lista "b".
    La lista modificada no depende del nombre del parámetro en la función (que es "b"), sino de la 
    variable enviada como argumento ("a" o "b").
'''

# def cambia(b):
#     b += [5]
#     return
# a, b = [3], [4]
# print(f"Al principio        : a = {a} b = {b}")
# cambia(a)
# print(f"Después de cambia(a): a = {a} b = {b}")
# cambia(b)
# print(f"Después de cambia(b): a = {a} b = {b}")
# print("Programa terminado")

'''
    Ejemplo de conflicto entre nombre de parámetro y nombre de variable global. Objeto inmutable
    Como en este caso las variables son números enteros (objetos inmutables), la función no puede
    modificar los números que se envían como argumentos, ni la variable "a" ni la variable "b".
'''

# def cambia(b):
#     b += 1
#     return
# a, b = 3, 4
# print(f"Al principio        : a = {a} b = {b}")
# cambia(a)
# print(f"Después de cambia(a): a = {a} b = {b}")
# cambia(b)
# print(f"Después de cambia(b): a = {a} b = {b}")
# print("Programa terminado")


'''
    Paso por valor o paso por referencia:
    
    En los lenguajes en los que las variables son "cajas" en las que se guardan valores, cuando
    se envía una variable como argumento en una llamada a una función suelen existir dos posibilidades:
        • paso por valor: se envía simplemente el valor de la variable, en cuyo caso la función no
            puede modificar la variable, pues la función sólo conoce su valor, pero no la variable que
            lo almacenaba.
        • paso por referencia: se envía la dirección de memoria de la variable, en cuyo caso la función
            sí que puede modificar la variable.
    En Python no se hace ni una cosa ni otra. En Python cuando se envía una variable como argumento en
    una llamada a una función lo que se envía es la referencia al objeto al que hace referencia la
    variable. Dependiendo de si el objeto es mutable o inmutable, la función podrá modificar o no el objeto
    
    
    En el ejemplo siguiente, la variable enviada a la función es una variable que hace referencia a un 
    objeto inmutable.
'''

# def aumenta(x):
#     print(id(x))
#     x += 1
#     print(id(x))
#     return x
# a = 3
# print(id(3), id(4))
# print(id(a))
# print(aumenta(a))
# print(a)
# print(id(a))


'''
    En el ejemplo siguiente, la variable enviada a la función es una variable que hace referencia a un
    objeto mutable.
'''

# def aumenta(x):
#     print(id(x))
#     x += [1]
#     print(id(x))
#     return x
# a = [3]
# print(id(a))
# print(aumenta(a))
# print(a)
# print(id(a))

# def fun(arg=1):
#     arg += 1
#     print(arg)
# arg = 3
# fun()

# die = 'yira te amo'
# print(die.count('a'))

# Quiz Funciones
# import math
# def proyectil(theta, v_o):
#     angulo_radianes = theta * (math.pi/180)
#     x_max = (v_o ** 2) * math.sin(2 * angulo_radianes) / 9.8
#     y_max = (v_o ** 2) * (math.sin(angulo_radianes)) ** 2 / (2 * 9.8)
#     return x_max, y_max
# print(proyectil(0, 0))

# archivo = 'datos.txt'
# print(archivo.split('.'))
#
# 1 e-> 4491.96
#  x  -> 4500

# def peso_a_euro(valor):
#     convert = valor / 4491.96
#     return convert
# print(peso_a_euro(0))

# def suma(a, b):
#     return a+b
# print(suma(4, 3))

# import math
# def area_triangulo(a, b, c):
#     s = (a + b + c) / 2
#     area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#     return area
# print(area_triangulo(0, 0, 0))





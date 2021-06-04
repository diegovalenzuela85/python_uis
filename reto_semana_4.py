'''

Planteamiento de la situación



En una granja acaban de adquirir una máquina que le permitirá a una empresa de huevos aumentar la rapidez con la que son
dispuestos sus productos para la distribución al usuario final. Se requiere un ingeniero de sistemas  para que programe
esta máquina bajo ciertos estándares.

Los huevos son clasificados según su calidad y su peso. Para identificar la calidad de los huevos existen tres
categorías A, B y C. Los huevos de categoría A son huevos frescos sin defectos y aptos para el consumo humano.
Los huevos de categoría B son huevos de calidad normal que han sido sometidos a procesos de conservación. Los
huevos tipo C son huevos que deben ser pasados por procesos industriales para ser considerados aptos para el consumo.

Los huevos de categoría A son clasificados según su peso como:
Huevos A cuyo peso va desde los 53 g. hasta un peso menor de 60 g.
Huevos AA cuyo peso va desde los 60 g. hasta un peso menor de 67 g.
Huevos AAA cuyo peso está por encima de los 67 g.
y los tipo B y C o BC como:
Huevos B cuyo peso va desde 46 g. hasta un peso menor de 53 g.
Huevos C cuyo peso es menor de 46 g.

Escriba una función llamada clasificacion_huevos que de entrada, reciba una lista de datos tipo flotantes asociada al
peso de un conjunto de huevos. La lista puede tener cualquier número de datos. Un ejemplo de esta lista de datos puede
ser: [46.5, 60.8, 58.7, 70.0, 49.8]

donde cada ítem como se mencionó, está asociado al peso de cada huevo, es decir el primer ítem pertenece a un huevo que
pesa 46.5 gr.

La función debe ser capaz de clasificar los huevos de acuerdo al peso que se especifique en la lista anteriormente
mencionada. Los huevos deben ser clasificados si son A, AA, AAA o si son BC (Una única clasificación para los huevos B
y C). Es decir el primer huevo pesa 46.5 gr lo que indica que el huevo es de categoría BC.

Al clasificar los huevos determine el total de huevos de cada uno de los tipos de huevos, A, AA, AAA y BC. Habiendo
determinado el número de huevos de acuerdo a cada clasificación, desarrolle una función adicional, llamada
calcular_bandejas, que permita calcular cuántas bandejas de huevos se pueden obtener para cada una de las categorías,
considerando que los huevos tipo A se empacan en grupos de 30 huevos, los tipo AA en grupos de 24 huevos, los tipo AAA
en grupos de 12 huevos y los tipo BC en grupos de 30 huevos. Esta función debe recibir como parámetro de entrada el
número de huevo y los huevos por bandeja.

La función clasificacion_huevos debe retornar una lista de directorios con la siguiente información y estructura:

[

{‘tipo_huevos’: ‘A’, ‘numero_huevos’: 70, ‘numero_bandejas’: 2},

{‘tipo_huevos’: ‘AA’, ‘numero_huevos’: 120, ‘numero_bandejas’: 4},

{‘tipo_huevos’: ‘AAA’, ‘numero_huevos’: 170, ‘numero_bandejas’: 5},

{‘tipo_huevos’: ‘BC’, ‘numero_huevos’: 80, ‘numero_bandejas’: 2}

]

Debe tenerse en cuenta el orden de cada una de las distintas clases de huevos. Tenga en cuenta que los huevos tipo BC
son la unión de los huevos tipo B y los tipo C.



Planteamiento del reto

Con respecto a lo planteado anteriormente, ¿Cómo se podría automatizar el proceso de clasificación de huevos mediante
el uso de una función escrita en Python de tal manera que a partir de un conjunto de datos relacionados con el peso de
un conjunto de huevos, se llegue a la clasificación de huevos tipo A, AA, AAA, y B y C? Adicionalmente, ¿Cómo se podría
definir una segunda función que permita calcular cuántas bandejas de huevos se pueden obtener por cada una de las
clasificaciones?

Acciones de aprendizaje

Entienda claramente cuál es la problemática que se requiere resolver y para qué se quiere hacer.

Identifique y declare todas las variables necesarias para llevar a cabo cada una de las clasificaciones correspondientes.

Identifique y declare todas las variables necesarias para almacenar la información que se requiere precisar.

Identifique la funcionalidad que debe tener el algoritmo a desarrollar dentro de la función.

A partir de los puntos anteriores escriba la función en Python que permita tomar los parámetros de entrada y procesarlos,
de tal manera que al final retorne los valores establecidos en el enunciado, en el orden en que se han especificado.

'''

import random

huevos_ingreso = int(input('Ingresa la cantidad de huevos dispuesta: '))
pesos_menor_huevos, pesos_mayor_huevos = 40, 70
lista_huevos, lista_huevos_a, lista_huevos_aa, lista_huevos_aaa, lista_huevos_bc = [], [], [], [], []
for huevos in range(huevos_ingreso):
    huevo_peso = round(random.uniform(pesos_menor_huevos, pesos_mayor_huevos), 2)
    lista_huevos.append(huevo_peso) # Lista de huevos con su respectivo peso
# print(lista_huevos) # IMPRIMIMOS Lista de huevos con su respectivo peso
# print(f"Cantidad de huevos: {len(lista_huevos)}") # IMPRIMIMOS Cantidad huevos en Lista
#
# def clasificacion_huevos(lista_huevos):
#     for huevo in lista_huevos:
#         if huevo >= 53 and huevo < 60:
#             lista_huevos_a.append(huevo)
#         elif huevo >= 60 and huevo < 67:
#             lista_huevos_aa.append(huevo)
#         elif huevo >= 67:
#             lista_huevos_aaa.append(huevo)
#         else:
#             lista_huevos_bc.append(huevo)
#
#     def calcular_bandejas(cantidad, bandeja):
#         bandejas = cantidad // bandeja
#         return bandejas
#
#     bandejas_a = 30
#     bandejas_aa = 24
#     bandejas_aaa = 12
#     bandejas_bc = 30
#
#     cta_huevos_a = len(lista_huevos_a)
#     cta_huevos_aa = len(lista_huevos_aa)
#     cta_huevos_aaa = len(lista_huevos_aaa)
#     cta_huevos_bc = len(lista_huevos_bc)
#
#     global lista_salida
#
#     lista_salida = []
#
#     total_bandejas_a = calcular_bandejas(cta_huevos_a, bandejas_a)
#     total_bandejas_aa = calcular_bandejas(cta_huevos_aa, bandejas_aa)
#     total_bandejas_aaa = calcular_bandejas(cta_huevos_aaa, bandejas_aaa)
#     total_bandejas_bc = calcular_bandejas(cta_huevos_bc, bandejas_bc)
#
#     datos_salida_a = {'tipo_huevos': 'A', 'numero_huevos': cta_huevos_a, 'numero_bandejas': total_bandejas_a}
#     lista_salida.append(datos_salida_a)
#     datos_salida_aa = {'tipo_huevos': 'AA', 'numero_huevos': cta_huevos_aa, 'numero_bandejas': total_bandejas_aa}
#     lista_salida.append(datos_salida_aa)
#     datos_salida_aaa = {'tipo_huevos': 'AAA', 'numero_huevos': cta_huevos_aaa, 'numero_bandejas': total_bandejas_aaa}
#     lista_salida.append(datos_salida_aaa)
#     datos_salida_bc = {'tipo_huevos': 'BC', 'numero_huevos': cta_huevos_bc, 'numero_bandejas': total_bandejas_bc}
#     lista_salida.append(datos_salida_bc)
#     #print(lista_salida)
#     return lista_salida
#
# clasificacion_huevos(lista_huevos)
# print(lista_salida)


#____________________________________________________________________________________________________________________

# import  math
# def clasificacion_huevos(lista_peso_huevos):
#     huevo_tipo_a = 0
#     huevo_tipo_aa = 0
#     huevo_tipo_aaa = 0
#     huevo_tipo_bc = 0
#     for huevo in lista_peso_huevos:
#         if huevo >= 53 and huevo < 60:
#             huevo_tipo_a += 1
#         elif huevo >= 60 and huevo < 67:
#             huevo_tipo_aa += 1
#         elif huevo >= 67:
#             huevo_tipo_aaa += 1
#         else:
#             huevo_tipo_bc += 1
#     def calcular_bandejas(huevo_tipo_a, huevo_tipo_aa, huevo_tipo_aaa, huevo_tipo_bc):
#         bandejas_tipo_a = math.floor(huevo_tipo_a/30)
#         bandejas_tipo_aa = math.floor(huevo_tipo_aa/24)
#         bandejas_tipo_aaa = math.floor(huevo_tipo_aaa/12)
#         bandejas_tipo_bc = math.floor(huevo_tipo_bc/30)
#         return bandejas_tipo_a, bandejas_tipo_aa, bandejas_tipo_aaa, bandejas_tipo_bc
#     bandejas_tipo_a, bandejas_tipo_aa, bandejas_tipo_aaa, bandejas_tipo_bc = calcular_bandejas(huevo_tipo_a, huevo_tipo_aa, huevo_tipo_aaa, huevo_tipo_bc)
#     diccionario_a ={'tipo_huevos': 'A', 'numero_huevos': huevo_tipo_a, 'numero_bandejas': bandejas_tipo_a}
#     diccionario_aa ={'tipo_huevos': 'AA', 'numero_huevos': huevo_tipo_aa, 'numero_bandejas': bandejas_tipo_aa}
#     diccionario_aaa ={'tipo_huevos': 'AAA', 'numero_huevos': huevo_tipo_aaa, 'numero_bandejas': bandejas_tipo_aaa}
#     diccionario_bc ={'tipo_huevos': 'BC', 'numero_huevos': huevo_tipo_bc, 'numero_bandejas': bandejas_tipo_bc}
#     lista_diccionarios_salida = [diccionario_a, diccionario_aa, diccionario_aaa, diccionario_bc]
#     return lista_diccionarios_salida
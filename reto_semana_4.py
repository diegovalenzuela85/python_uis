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

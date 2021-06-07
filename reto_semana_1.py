# Planteamiento de la situación
#
#
# ¡Qué bueno! Acabas de recibir tu primer salario luego de una ardua jornada de trabajo. Piensas por unos
# instantes en lo que vas hacer con el dinero que has recibido. De manera casi inmediata, vienen a tu mente
# varias ideas; sin embargo, decides rápidamente la forma en la que distribuirás el dinero. Un 20 % para compra
# de alimentos, 15% para compra de pasajes, 10% para compra de boletos de cine, 15% para compra de libros y el
# dinero restante debe ser destinado para el pago del alquiler del lugar donde estás viviendo.
#
#
#
# Planteamiento del reto
#
#
# Con respecto a la situación planteada, ¿De qué manera crees que se puede llegar a automatizar el proceso
# descrito desde un lenguaje de programación, de tal forma que no tengas que volver a realizar los cálculos
# de presupuesto cada vez que te llegue un salario?
#
#
#
# Acciones de aprendizaje
#
#
# a. Identifica y declara las variables que consideres necesarias para realizar los cálculos correspondientes
# y/o asignaciones directas.
#
# b. A partir de las variables definidas anteriormente, escribe el código requerido para mostrar el presupuesto
# asignado a cada categoría, tal como se muestra a continuación:
#
#
#
# Salida: El resultado corresponde a un número que refleja el saldo luego de realizar las compras.
#
#
#
# Solución del reto
# Soluciona el reto, escribiendo el código que represente la automatización del proceso del cálculo del presupuesto.

salario = int(input())
alimentos = salario * 0.2
pasajes = salario * 0.1
cine = salario * 0.05
libros = salario * 0.05
alquiler = salario - alimentos - pasajes - cine - libros
print(alquiler)
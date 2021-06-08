'''
    Planteamiento de la situación:

    Acabas de ver la última consola de videojuegos y piensas que debe ser tuya como sea. Como ya has pedido
    dinero a tus padres en los últimos meses, piensas en ahorrar por tu propia cuenta el dinero para comprarla,
    aprovechando tu trabajo de mensajero.

    Ya han pasado varios meses y en tu agenda de ahorro tienes los siguientes datos: los aportes de los meses
    de enero, febrero, marzo y abril. Durante el mes de enero tuviste tres aportes, en febrero dos, en marzo
    nuevamente tres y en abril, cuatro aportes. Descubres que tus amigos, llevan la misma estrategia de ahorro
    y decides facilitar el proceso de cálculo de los valores ahorrados mensualmente.

    Aprovechando que has iniciado un curso de programación, decides automatizar el proceso para impresionar
    a tus amigos sobre la forma efectiva y rápida de hacer estos cálculos.

    Planteamiento del reto:

    ¿De qué manera podrías organizar los datos de tal manera que puedas obtener automáticamente el ahorro
    que has hecho tú y tus amigos por cada mes?

    Acciones de aprendizaje

    1 - Identifica los tipos de datos que tienes.
    2 - Define la estructura de datos más adecuada para representarlos.
    3 - Utiliza la estructura de datos definida para encontrar la suma total de los ahorros por cada mes.
    4 - Como el proceso se puede repetir para ti y cada uno de tus amigos, define una función que reciba
        como parámetros una cadena de texto con el siguiente formato:
        "Enero,4,3,4;Febrero,4,3;Marzo,4,3,4;Abril,4,3,4,4"
        para los registros de ahorro y un segundo parámetro con el nombre de la persona a quien se le
        hará el cálculo. Por ejemplo: calculadoraMes(registroDeAhorros,nombre)
    5 - Retorna la respuesta con el siguiente formato por ejemplo para las entradas
        calculadoraMes("Enero,4,3,4;Febrero,4,3;Marzo,4,3,4;Abril,4,3,4,4" ,"daniel")
        la salida sería ('daniel', {'Enero': 11, 'Febrero': 7, 'Marzo': 11, 'Abril': 15})

    Solución del reto:

    Solucione este reto escribiendo el código que permite resolver el problema planteado.
'''


# registroDeAhorros = "Enero,4,3,4;Febrero,4,3;Marzo,4,3,4;Abril,4,3,4,4"
# def calculadoraMes(registroDeAhorros,nombre):
#     separa_punto_coma = registroDeAhorros.split(';')
#     mes0, mes1, mes2, mes3, mes4, mes5, mes6, mes7, mes8, mes9, mes10, mes11 = "", "", "", "", "", "", "", "", "", "", "", ""
#     list_num0, list_num1, list_num2, list_num3, list_num4, list_num5, list_num6, list_num7, list_num8, list_num9, list_num10, list_num11 = [], [], [], [], [], [], [], [], [], [], [], []
#     for cadena in range(len(separa_punto_coma)):
#         if cadena == 0:
#             mes0 = separa_punto_coma[cadena]
#             sin_coma0 = mes0.split(',')
#             mes0 = sin_coma0.pop(0)
#             list_num0 = [int(i) for i in sin_coma0]
#         elif cadena == 1:
#             mes1 = separa_punto_coma[cadena]
#             sin_coma1 = mes1.split(',')
#             mes1 = sin_coma1.pop(0)
#             list_num1 = [int(i) for i in sin_coma1]
#         elif cadena == 2:
#             mes2 = separa_punto_coma[cadena]
#             sin_coma2 = mes2.split(',')
#             mes2 = sin_coma2.pop(0)
#             list_num2 = [int(i) for i in sin_coma2]
#         elif cadena == 3:
#             mes3 = separa_punto_coma[cadena]
#             sin_coma3 = mes3.split(',')
#             mes3 = sin_coma3.pop(0)
#             list_num3 = [int(i) for i in sin_coma3]
#         elif cadena == 4:
#             mes4 = separa_punto_coma[cadena]
#             sin_coma4 = mes4.split(',')
#             mes4 = sin_coma4.pop(0)
#             list_num4 = [int(i) for i in sin_coma4]
#         elif cadena == 5:
#             mes5 = separa_punto_coma[cadena]
#             sin_coma5 = mes5.split(',')
#             mes5 = sin_coma5.pop(0)
#             list_num5 = [int(i) for i in sin_coma5]
#         elif cadena == 6:
#             mes6 = separa_punto_coma[cadena]
#             sin_coma6 = mes6.split(',')
#             mes6 = sin_coma6.pop(0)
#             list_num6 = [int(i) for i in sin_coma6]
#         elif cadena == 7:
#             mes7 = separa_punto_coma[cadena]
#             sin_coma7 = mes7.split(',')
#             mes7 = sin_coma7.pop(0)
#             list_num7 = [int(i) for i in sin_coma7]
#         elif cadena == 8:
#             mes8 = separa_punto_coma[cadena]
#             sin_coma8 = mes8.split(',')
#             mes8 = sin_coma8.pop(0)
#             list_num8 = [int(i) for i in sin_coma8]
#         elif cadena == 9:
#             mes9 = separa_punto_coma[cadena]
#             sin_coma9 = mes9.split(',')
#             mes9 = sin_coma9.pop(0)
#             list_num9 = [int(i) for i in sin_coma9]
#         elif cadena == 10:
#             mes10 = separa_punto_coma[cadena]
#             sin_coma10 = mes10.split(',')
#             mes10 = sin_coma10.pop(0)
#             list_num10 = [int(i) for i in sin_coma10]
#         elif cadena == 11:
#             mes11 = separa_punto_coma[cadena]
#             sin_coma11 = mes11.split(',')
#             mes11 = sin_coma11.pop(0)
#             list_num11 = [int(i) for i in sin_coma11]
#     respuesta = (nombre, {mes0: sum(list_num0), mes1: sum(list_num1), mes2: sum(list_num2), mes3: sum(list_num3)})
#     return respuesta
#     # print(list_num0)
#     # print(f'mes1: {mes0} \nmes2: {mes1} \nmes3: {mes2} \nmes4: {mes3} \n')
#
# # ('daniel', {'Enero': 11, 'Febrero': 7, 'Marzo': 11, 'Abril': 15})
#
# print(calculadoraMes("Enero,4,3,4;Febrero,4,3;Marzo,4,3,4;Abril,4,3,4,4", "daniel"))

# import re
# cadena = "Enero,4,3,4;Febrero,4,3;Marzo,4,3,4;Abril,4,3,4,4"
# cadena_mayus = cadena.upper()
# lista_sin_coma = cadena_mayus.split(';')
# print(lista_sin_coma)
# enero = lista_sin_coma[0]
# febrero = lista_sin_coma[1]
# marzo = lista_sin_coma[2]
# abril = lista_sin_coma[3]
# enero_sin_mes = re.split('\D+', enero)
# febrero_sin_mes = re.split('\D+', febrero)
# marzo_sin_mes = re.split('\D+', marzo)
# abril_sin_mes = re.split('\D+', abril)
# sum_enero = 0
# def suma_meses(lista_sin_mes):
#     resultado_sum = 0
#     for num in lista_sin_mes:
#         if num != '':
#             num = int(num)
#             resultado_sum += num
#     return resultado_sum
# suma_enero = suma_meses(enero_sin_mes)
# suma_febrero = suma_meses(febrero_sin_mes)
# suma_marzo = suma_meses(marzo_sin_mes)
# suma_abril = suma_meses(abril_sin_mes)
#
# print(f"Esto es sum_enero {sum_enero}")
# print(f"Esto es resultado_sum {suma_enero}")
# print(f"Esto es la lista sin mes {enero_sin_mes}")
# print(f'{enero} <-> {febrero} <-> {marzo} <-> {abril}')
#
#
# import re
# cadena = "Enero,4,3,4;Febrero,4,3;Marzo,4,3,4;Abril,4,3,4,4"
# lista_sin_punto_coma = cadena.split(';')
# cuenta = int(len(lista_sin_punto_coma))
# mes_01 = []
# for cta in range(cuenta):
#     for i in (lista_sin_punto_coma):
#         mes = lista_sin_punto_coma[cta]
#     print(mes)
#
#
#
# def calculadoraMes(cadena):
#     mes0, mes1, mes2, mes3, mes4, mes5, mes6, mes7, mes8, mes9, mes10, mes11 = "", "", "", "", "", "", "", "", "", "", "", ""
#     lista_sin_punto_coma = cadena.split(';')
#     cuenta = int(len(lista_sin_punto_coma))
#     for cta in range(cuenta):
#         # print(cta)
#         # print(type(cta))
#         for i in (lista_sin_punto_coma):
#             if cta == 0:
#                 mes0 = lista_sin_punto_coma[cta]
#             elif cta == 1:
#                 mes1 = lista_sin_punto_coma[cta]
#             elif cta == 2:
#                 mes2 = lista_sin_punto_coma[cta]
#             elif cta == 3:
#                 mes2 = lista_sin_punto_coma[cta]
#     print(mes0)
#
#
# calculadoraMes(cadena)


# def calculadoraMes(registroDeAhorros,nombre):
#     separa_punto_coma = registroDeAhorros.split(';')
#     mes0, mes1, mes2, mes3 = "", "", "", ""
#     list_num0, list_num1, list_num2, list_num3 = [], [], [], []
#     for cadena in range(len(separa_punto_coma)):
#         if cadena == 0:
#             mes0 = separa_punto_coma[cadena]
#             sin_coma0 = mes0.split(',')
#             mes0 = sin_coma0.pop(0)
#             list_num0 = [int(i) for i in sin_coma0]
#         elif cadena == 1:
#             mes1 = separa_punto_coma[cadena]
#             sin_coma1 = mes1.split(',')
#             mes1 = sin_coma1.pop(0)
#             list_num1 = [int(i) for i in sin_coma1]
#         elif cadena == 2:
#             mes2 = separa_punto_coma[cadena]
#             sin_coma2 = mes2.split(',')
#             mes2 = sin_coma2.pop(0)
#             list_num2 = [int(i) for i in sin_coma2]
#         elif cadena == 3:
#             mes3 = separa_punto_coma[cadena]
#             sin_coma3 = mes3.split(',')
#             mes3 = sin_coma3.pop(0)
#             list_num3 = [int(i) for i in sin_coma3]
#     respuesta = (nombre, {mes0: sum(list_num0), mes1: sum(list_num1), mes2: sum(list_num2), mes3: sum(list_num3)})
#     return respuesta
# print(calculadoraMes("Enero,4,3,4;Febrero,4,3;Marzo,4,3,4;Abril,4,3,4,4", "daniel"))

def palabras(cadena):
    lista = cadena.split(',')
    return lista

print(palabras("Inglés,Física, Sociales,Historia,Programación"))
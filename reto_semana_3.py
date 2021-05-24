# Planteamiento de la situación
#
#
#
#
#
# Clasificado: La compañía de software Misión TIC 2022, que se dedica al desarrollo de aplicaciones computacionales para empresas de diversos sectores, desea contratar programadores en lenguaje Python que implementen una aplicación para gestionar de manera automatizada el control y registro de empleados y visitantes en una organización.  Has visto el anterior clasificado y decides visitar la compañía. Durante la entrevista, el supervisor te informa en qué consiste la tarea que debes emprender porque desea dejar de lado el cuaderno de registro que actualmente utiliza.
#
#
#
#
#
# Planteamiento del reto
#
#
#
#
#
# ¿De qué manera puedes ayudar a la organización para automatizar los registros que actualmente se llevan a cabo de manera manual?
#
#
#
#
#
#
#
# Acciones de aprendizaje
#
#
#
#
#
#
#
# a. Analizar, identificar y declarar las variables que considere necesarias para realizar la administración de los ingresos de los empleados y visitantes.
# b. Determinar desde las variables identificadas, cual(es) corresponden a los datos de entrada, las operaciones entre ellas que dan solución al reto, y cual(es) son los datos para presentar como salida.
# c. Diseñar el algoritmo desde un lenguaje de programación que facilite las tareas de automatización, depuración y verificación de la solución propuesta.
#
#
#
#
# Solución del reto
#
#
#
#
#
# El aplicativo debe cumplir los siguientes requerimientos:
#
#
#
# 1. Solicitar usuario y contraseña validando que las credenciales sean correctas y permitiendo tres intentos máximos. Luego de los tres intentos fallidos se debe cerrar el aplicativo; el usuario predefinido es admin y la contraseña será MisionTic2021 .
#
# 2. Si el ingreso es exitoso, se debe mostrar un menú con las siguientes opciones:
#
# - 1. Registrar ingreso de empleado.
#
# - 2. Ver empleados ingresados.
#
# - 3. Registrar ingreso de visitantes.
#
# - 4. Ver visitantes ingresados.
#
# - 0. Salir.
#
# 3. El menú debe mostrarse hasta que el usuario digite una opción válida o determine salir.
#
# 4. Al seleccionar las opciones 1 y 3, se deben guardar el registro de quién ingresa de manera iterativa, es decir, el usuario podrá registrar tantos empleados y visitantes como se requieran, sin necesidad de ingresar cada vez al menú. Se dejará de ingresar empleados o visitantes cuando el usuario no incluya ninguno y oprima la tecla enter.
#
# 5. Al seleccionar las opciones 2 y 4, se debe visualizar los empleados y visitantes según corresponda, separados por comas (,).
#
#
#
#
#
# Solución del reto
#
#
#
#
#
# Solucione el reto, escribiendo el código que represente la automatización del proceso de registro de empleados y visitantes.

ingreso_usuario = input("Usuario: ")
ingreso_contrasena = input("Contraseña: ")

usuario = "admin"
contrasena = "MisionTic2021"
empleados = ""
visitantes = ""

intentosLogin = 1

while usuario != ingreso_usuario or contrasena != ingreso_contrasena:
    if intentosLogin == 4:
        print("Credenciales incorrectas")
        print("Has agotado la cantidad de intentos, por favor inicie de nuevo el programa")
        break
    else:
        print("Credenciales incorrectas")
        ingreso_usuario = input("Usuario: ")
        ingreso_contrasena = input("Contraseña: ")
        intentosLogin += 1

if usuario == ingreso_usuario and contrasena == ingreso_contrasena:
    while True:
        print()
        print("------Menú de registro de personal-----")
        print("1. Registrar ingreso de empleado.")
        print("2. Ver empleados ingresados.")
        print("3. Registrar ingreso de visitantes.")
        print("4. Ver visitantes ingresados.")
        print()
        print("0. Salir")
        print()
        seleccion = int(input("Ingresa un número válido de opción del menú: "))
        if seleccion == 1:
            empleados = ""
            while True:
                nombre = input("Ingresa el nombre del empleado (Si no deseas agregar más, oprime la tecla SALIR): ")
                if nombre == "SALIR":
                    break
                else:
                    empleados += nombre
                    empleados += ","
        if seleccion == 2:
            print("Los empleados registrados son:", empleados)
        elif seleccion == 3:
            visitantes = ""
            while True:
                nombre = input("Ingresa el nombre del visitante (Si no deseas agregar más, digite SALIR): ")
                if nombre == "SALIR":
                    break
                else:
                    visitantes += nombre
                    visitantes += ","
        elif seleccion == 4:
            print("Los visitantes registrados son:", visitantes)
        elif seleccion == 0:
            print("¡Hasta luego!")
            break
        elif seleccion != 1 and seleccion != 2 and seleccion != 3 and seleccion != 4 and seleccion != 0:
            print("Por favor ingresa una opción válida")

# if usuario != ingreso_usuario and contrasena != ingreso_contrasena:
#     print()
#     print('Adios,no pudiste ingresar.')


# while True:
#     print()
#     print('1. Registrar ingreso de empleado.')
#     print('2. Ver empleados ingresados')
#     print('3. Registrar ingreso de visitantes.')
#     print('4. Ver visitantes ingresados.')
#     print('0 . Salir.')
#     seleccion = int(input('Ingresa el numero correspondiente: '))
#     if seleccion == 1:
#         print('estas en 1')
#         data = ''
#         nombre = ''
#         while True:
#             nombre = input('Ingresa un nombre: ')
#             if nombre == '':
#                 break
#             else:
#                 data += nombre
#                 data += ", "
#     if seleccion == 2:
#         print(f'Tienes guardados estos nombres: {data}')
#     elif seleccion == 3:
#         while True:
#             nombre = input('Ingresa un nombre: ')
#             if nombre == '':
#                 break
#             else:
#                 data += nombre
#                 data += ", "
#     elif seleccion == 4:
#         print('estas en 4')
#         print(f'Tienes guardados estos nombres: {data}')
#     elif seleccion == 0:
#         print()
#         print('Saliste... muchas gracias')
#         break
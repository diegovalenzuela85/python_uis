salario = int(input())
alimentos = salario * 0.2
pasajes = salario * 0.1
cine = salario * 0.05
libros = salario * 0.05
alquiler = salario - alimentos - pasajes - cine - libros
print(alquiler)
posicion=0
while posicion<=0:
    posicion=int(input('Ingrese la posición a generar la serie de Fibonacci debe ser mayor a 0:'))
if posicion==1:
    Serie_fibonacci='0'
    fibonacci=0
elif posicion==2:
    Serie_fibonacci='0,1'
    fibonacci=1
else:
    fibonacci_1=0
    fibonacci_2=1
    Serie_fibonacci='0,1'
    for i in range(posicion-2):
        fibonacci=fibonacci_2+fibonacci_1
        fibonacci_1=fibonacci_2
        fibonacci_2=fibonacci
        Serie_fibonacci=Serie_fibonacci+','+str(fibonacci)
print('El fibonacci de la posición:',posicion,'es',fibonacci)
print('La seria Fibonacci hasta la posición:',posicion,'es',Serie_fibonacci)
            

'''
0,1,1,2,3,5,8,13,21,34,55,89,144,…
1==>0
2==>1
3==>0+1=1
4==>1+1=2
5==>2+1=3
6==>3+2=5
7==>5+3=8 
'''

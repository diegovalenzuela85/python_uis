peso = float(input())
estatura = float(input())
if peso > 0 and estatura > 0:
    imc = peso / (estatura) ** 2
    if 0 <= imc < 18.5:
        print('Bajo peso')
    elif 18.5 <= imc <= 24.9:
        print('Normal')
    elif 25 <= imc <= 29.9:
        print('Sobrepeso')
    else:
        print('Obeso')

# EJERCICIO str()

## Diseñar el algoritmo correspondiente a un programa que al introducir una cantidad de dinero expresado
# en pesos nos indique cuántos billetes y monedas se puede tener como mínimo (Billetes de 1000, 2000, 5000,
# 10000, 20000 y 50000, monedas de 20, 50, 100, 200 y 500).

monto = int(input('Ingresa el monto a calcular: '))
d_billetes = [50000,20000,10000,5000,2000,1000]
d_monedas = [500,200,100,50,20]
billetes = ""
monedas = ""

for b in d_billetes:
    billete = int(monto // b)
    if billete > 0:
        #billetes += f"({b},{billete}) "
        #billetes += "(" + str(b) + "," + str(billete) + ")"
        #billetes += "(" + "Necesito " + str(billete) + " Billetes de " + str(b) + " pesos\n"
        billetes += f"Necesito {billete} Billetes de {b} pesos\n"
        monto -= (b * billete)
for m in d_monedas:
    moneda = int(monto // m)
    if moneda > 0:
        #monedas += f"({m},{moneda}) "
        #monedas += "(" + str(m) + "," + str(moneda) + ")"
        monedas += "Necesito " + str(moneda) + " Monedas de " + str(m) + " pesos\n"
        monto -= (m * moneda)

print(f'{billetes}{monedas}')


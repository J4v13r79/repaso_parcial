'''Un vendedor gana 5% de comisión sobre sus ventas del mes. Si vende $10,000 o más, la comisión es de 
8%. Si vende más de $50,000, recibe además un bono de $1,000. Se necesita mostrar la comisión, el bono 
y el total a pagar.'''

# PROBLEMA 
# Qué se calcula, La comisión, el bono y el total a pagar.

# ENTRADAS
# ventas : float, 0 < ventas < 100000

# SALIDAS
# comision : float, 0 < comision < 8000
# bono : float, 0 < bono < 1000
# total : float, 0 < total < 9000

# REGLAS Y SUPUESTOS 
# - Valores fijos del problema (tarifas, porcentajes, topes). 
# - Límites exactos de cada condición. 
# - Regla de redondeo. 
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió. 

# ALGORITMO
# 1. Leer ventas
# 2. Si ventas <= 10000:
#       comision = ventas * 0.05
#       bono = 0
# 3. Si ventas > 10000 y ventas <= 50000:
#       comision = ventas * 0.08
#       bono = 0
# 4. Si ventas > 50000:
#       comision = ventas * 0.08
#       bono = 1000
# 5. total = comision + bono
# 6. Mostrar comision, bono y total

# CASOS DE PRUEBA
# $5,000 -- 250$
# $10,000 -- 800$   
# $50,000 -- 4,000$
# $50,001 -- 5000.08$

# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# leerVentas: no recibe parámetros, retorna un float.
# calcularComision: recibe un float (ventas), retorna un float.
# calcularBono : recibe un float (ventas), retorna un float.
# mostrarPago : recibe tres float (comision, bono, total), no retorna nada.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerVentas():
    ventas = float(input("Ingrese el monto de ventas del mes: "))
    return ventas

def calcularComision(ventas):
    if ventas <= 10000:
        comision = ventas * 0.05 
    elif ventas <= 50000:
        comision = ventas * 0.08 
    else:
        comision = ventas * 0.08 
    return comision

def calcularBono(ventas):
    if ventas > 50000:
        bono = 1000
    else:
        bono = 0
    return bono

def mostrarPago(comision, bono, total):
    print(f"Comisión: {comision:.2f}")
    print(f"Bono: {bono:.2f}")
    print(f"Total a pagar: {total:.2f}")
'''Un taxi cobra $35 de banderazo y $9 por kilómetro recorrido. Los viajes de más de 20 km tienen 10% de 
descuento. Se necesita mostrar el importe del viaje.'''

# PROBLEMA 
# Qué se calcula, el importe del viaje.

# ENTRADAS
# kilometros : float, 0 < kilometros < 1000

# SALIDAS
# importe_viaje : float, 0 < importe_viaje < 10000

# REGLAS Y SUPUESTOS 
# - Valores fijos del problema (tarifas, porcentajes, topes). 
# - Límites exactos de cada condición. 
# - Regla de redondeo. 
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió. 

# ALGORITMO
# 1. Leer kilometros
# 2. Si kilometros > 20:
#       importe_viaje = (35 + 9 * kilometros )* 0.9
# 3. En otro caso:
#       importe_viaje = 35 + 9 * kilometros
# 4. Mostrar importe_viaje

# CASOS DE PRUEBA
# (5) → importe del viaje: 80
# (20) → importe del viaje: 215
# (21) → importe del viaje: 204.30
# (30) → importe del viaje: 274.50

# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# leerKilometros : no recibe parámetros, retorna un float.
# calcularImporte: recibe un float (kilometros), retorna un float.
# mostrarImporte : recibe un float (importe), no retorna nada.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerKilometros():
    kilometros = float(input("Ingrese la cantidad de kilómetros recorridos: "))
    return kilometros

def calcularImporte(kilometros):
    if kilometros > 20:
        return (35 + 9 * kilometros) * 0.9
    else:
        return 35 + 9 * kilometros

def mostrarImporte(importe):
    print(f"El importe del viaje es: {importe:.2f}")
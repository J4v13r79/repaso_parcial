'''Una biblioteca cobra $5 por cada día de retraso en la devolución de un libro. A partir del día 11 de 
retraso, cada día cuesta $10. La multa máxima es de $200. Se necesita mostrar la multa a partir de los 
días de retraso. '''

# PROBLEMA 
# Qué se calcula, La multa.

# ENTRADAS
# dias_retraso : int, 0 < dias_retraso < 100

# SALIDAS
# multa : float, 0 < multa < 200

# REGLAS Y SUPUESTOS 
# - Valores fijos del problema (tarifas, porcentajes, topes). 
# - Límites exactos de cada condición. 
# - Regla de redondeo. 
# - Cada decisión que el enunciado no aclaraba y cómo se resolvió. 

# ALGORITMO
# 1. Leer dias_retraso
# 2. Si dias_retraso <= 10:
#       multa = dias_retraso * 5
#    Si no:
#       multa = 50 + (dias_retraso - 10) * 10
#    Si multa > 200:
#       multa = 200
# 3. Mostrar multa

# CASOS DE PRUEBA
# 0 días -- 0
# 10 días -- 50
# 11 días -- 60
# 25 días -- 200
# 40 días -- 200

# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# leerDias: no recibe parámetros, retorna un int.
# calcularMulta: recibe un int (dias_retraso), retorna un float.
# mostrarMulta: recibe un float (multa), no retorna nada.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerDias():
    dias_retraso = int(input("Ingrese la cantidad de días de retraso: "))
    return dias_retraso

def calcularMulta(dias_retraso):
    if dias_retraso <= 10:
        multa = dias_retraso * 5
    else:
        multa = 50 + (dias_retraso - 10) * 10
    if multa > 200:
        multa = 200
    return multa

def mostrarMulta(multa):
    print(f"La multa es: ${multa}")

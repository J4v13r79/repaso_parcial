from Ejercicios.ejercicio1_taxi import leerKilometros, calcularImporte, mostrarImporte
from Ejercicios.ejercicio2_comision import 
from Ejercicios.ejercicio3_biblioteca import 


def ejecutarEjercicio1():
    kilometros = leerKilometros()
    importe = calcularImporte(kilometros)
    mostrarImporte(importe)

 
def ejecutarEjercicio2(): 
    print("Ejercicio 2 pendiente.")

def ejecutarEjercicio3(): 
    print("Ejercicio 3 pendiente.")

def mostrarMenu():
    print()
    print("PRÁCTICA: DESARROLLO GUIADO POR ESPECIFICACIÓN") 
    print("1. Importe de viaje en taxi") 
    print("2. Comisión de ventas") 
    print("3. Multa de la biblioteca") 
    print("0. Salir") 
 
 
def menus(): 
    opcion = "" 
    while opcion != "0": 
        mostrarMenu() 
        opcion = input("Seleccione una opción: ") 
        if opcion == "1": 
            ejecutarEjercicio1() 
        elif opcion == "2": 
            ejecutarEjercicio2() 
        elif opcion == "3": 
            ejecutarEjercicio3()
        elif opcion != "0": 
            print("Opción no válida.")
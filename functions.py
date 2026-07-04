import os
import time
#acumuladores

#Listas
planes = {"F001":["Plan Básico","mensual",1, False, False, "libre"],
          "F002":["Plan Full","mensual", 1, False, False, "libre"]}
inscripciones = {"F001":[14990, 30],
                 "F002":[22990, 10]}

def limpiar():
    os.system("clear")

#validaciones

def validar_lista(lista): #como hay 2 listas usare verdadero o falso solo para validar si se puede realizar la operacion y desde main entregar un mensaje ya sea para planes o para inscripciones
    if len(lista) <= 0:
        return False
    else:
        return True

def validar_string(string):
    if len(string) > 0 and string != " ":
        return True
    else:
        print("El campo no puede ir vacio o solo ser un espacio.")

def validar_entero(entero):
    if entero > 0:
        return True
    else:
        print("El valor ingresado no puede ser menor o igual a 0.")

#Opcion 1
def cupos_tipo(tipo):
    acumulador_cupos = 0
    for x in planes:
        if tipo == planes[x][1]:
            acumulador_cupos = acumulador_cupos + inscripciones[x][1]
    print(f"\nEl total de cupos disponibles es: {acumulador_cupos}.")
        



#opcion 4

def agregar_plan():
    while True:
        codigo = input("Ingrese codigo plan:\n")
        if validar_string(codigo):

            break


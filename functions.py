import os
import time
#acumuladores

#Listas
planes = {"F001":["Plan Básico","mensual",1, False, False, "libre"],
          "F002":["Plan Full","mensual", 1, False, False, "libre"],
          "F003":["Plan Caquita","mensual", 1, False, False, "libre"]}
inscripciones = {"F001":[14990, 30],
                 "F002":[22990, 10],
                 "F003":[25990, 10]}

def limpiar():
    os.system("clear")

#validaciones

def validar_string(string):
    if len(string) > 0 and string != " ":
        return True
    else:
        print("El campo no puede ir vacio o solo ser un espacio.")


#Opcion 1
def cupos_tipo(tipo):
    acumulador_cupos = 0
    for x in planes:
        if tipo == planes[x][1]:
            acumulador_cupos = acumulador_cupos + inscripciones[x][1]
    print(f"\nEl total de cupos disponibles es: {acumulador_cupos}.")
        
#Opcion 2
def busqueda_precio(p_min, p_max):
    busqueda = []
    for x in inscripciones:
        if p_min <= inscripciones[x][0] and p_max >= inscripciones[x][0] and inscripciones[x][1] > 0:
            busqueda.append(f"{planes[x][0]}--{x}")
    if len(busqueda) > 0:
        busqueda.sort()
        print(f"Los planes encontrados son : {busqueda}")
    else:
        print("No se han encontrado planes en ese rango")

#Opcion 3
def actualizar_precio(codigo,nuevo_precio):
    for x in inscripciones:
        if codigo == x:
            inscripciones[x][0] = nuevo_precio
            return True
        else:
            return False
        
#opcion 4
def validar_codigo(codigo):
    
    if len(codigo) == 0 or codigo == " ":
        print("El codigo no puede ir vacio")
        return False
    for x in planes:
        if codigo == x:
            print("El codigo ingresado ya se encuentra registrado.")
            return False
    return True

def validar_nombre(nombre):
        if len(nombre) == 0 or nombre == " ":
            print("El nombre no puede ir vacio")
            return False
        else:
            return True
        
def validar_tipo(tipo):
    if tipo == "mensual" or tipo == "trimestral" or tipo == "anual":
        return True
    else:
        print("El tipo de plan solo puede ser: mensual, trimestral o anual.")
        return False
    
def validar_duracion(duracion):
    if duracion <= 0:
        print("La duracion no puede ser menor o igual a 0.")
        return False
    else:
        return True
    
def validar_acceso_piscina(acceso_piscina):
    if acceso_piscina == "S":
        return True
    elif acceso_piscina == "N":
        return True
    else:
        print("Opcion no valida.")
        return False

def validar_incluye_clases(incluye_clases):
    if incluye_clases == "S":
        return True
    elif incluye_clases == "N":
        return True
    else:
        print("Opcion no valida.")
        return False
    
def validar_horario(horario):
        if len(horario) == 0 or horario == " ":
            print("El horario no puede ir vacio")
            return False
        else:
            return True

def validar_precio(precio):
    if precio < 0:
        print("El precio no puede ser menor que 0.")
        return False
    else:
        return True

def validar_cupos(cupos):
    if cupos <= 0:
        print("Los cupos no puede ser menor o igual a 0.")
        return False
    else:
        return True

def agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos):
    planes[codigo] = [nombre, tipo, duracion, acceso_piscina, incluye_clases, horario]
    inscripciones[codigo] = [precio, cupos]

#opcion 5
def eliminar_plan(codigo):
    for x in planes:
        if codigo == x:
            planes.pop(x)
            inscripciones.pop(x)
            return True
    return False


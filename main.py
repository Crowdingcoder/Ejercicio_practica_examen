from functions import *

limpiar()
while True:
    print("========= MENU PRINCIPAL ===========")
    print("1. Cupos por tipo de plan")
    print("2. Busqueda de planes por rango de precio")
    print("3. Actualizar precio de plan")
    print("4. Agregar plan")
    print("5. Eliminar plan")
    print("6. Salir")
    print("====================================")

    menu = int(input("Ingrese opcion:\n"))
    if menu == 1:
        print("Menu 1")
        tipo = input("Ingrese tipo de plan a consultar: ").lower()
        cupos_tipo(tipo)

    elif menu == 2:
        print("Menu 2")
        while True:
            try:
                p_min = int(input("Ingrese precio minimo: "))
                p_max = int(input("Ingrese precio maximo: "))
                if p_min < 0 or p_max < 0:
                    print("Los valores ingresados no pueden ser menores a 0.")
                else:
                    busqueda_precio(p_min, p_max)
                    break
            except:
                print("Debe ingresar un  valor entero")

    elif menu == 3:
        print("menu 3")
        while True:
            codigo = input("Ingrese codigo del plan: ").upper()
            try:
                nuevo_precio = int(input("Ingrese nuevo precio: "))
                if nuevo_precio <= 0:
                    print("El valor ingresado no debe ser menor o igual a 0.")
                else:
                    if actualizar_precio(codigo,nuevo_precio):
                        print("Precio actualizado")
                    else:
                        print("El código no existe")
            except:
                print("El valor debe ser entero")
            
            continuar = input("¿Desea actualizar otro precio (s/n)?").upper()
            while continuar != "N" and continuar != "S":
                continuar = input("Opcion no valida.\n¿Desea actualizar otro precio (s/n)? ").upper()
            if continuar == "N":
                break
            elif continuar == "S":
                continue

    elif menu == 4:
        print("Menu 4")
        while True:
            codigo = input("Ingrese codigo del plan: ").upper()
            if validar_codigo(codigo) == False:
                break
            nombre = input("Ingrese nombre del plan :")
            if validar_nombre(nombre) == False:
                break
            tipo = input("Ingrese tipo (mensual/trimestral/anual): ").lower()
            if validar_tipo(tipo) == False:
                break
            try:
                duracion = int(input("Ingrese duración (meses): "))
                if validar_duracion == False:
                    break
            except:
                print("El valor ingresado solo puede ser entero.")
                break
            acceso_piscina = input("¿Incluye acceso a piscina? (s/n): ").upper()
            if validar_acceso_piscina(acceso_piscina) == False:
                break
            if acceso_piscina == "S":
                acceso_piscina = True
            elif acceso_piscina == "N":
                acceso_piscina = False
            incluye_clases = input("¿Incluye clases grupales? (s/n): ").upper()
            if validar_incluye_clases == False:
                break
            if incluye_clases == "S":
                incluye_clases = True
            elif incluye_clases == "N":
                incluye_clases = False
            horario = input("Ingrese horario: ").lower()
            if validar_horario == False:
                break
            try:
                precio = int(input("Ingrese precio: "))
                if validar_precio(precio) == False:
                    break
                cupos= int(input("Ingrese cupos: "))
                if validar_cupos == False:
                    break
            except:
                print("El valor ingresado debe ser entero.")
                break
            agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos)
            print("Plan agregado")
            print(planes)
            print(inscripciones)
            break

    elif menu == 5:
        print("Menu 5")
        codigo = input("Ingrese codigo del plan: ").upper()
        if eliminar_plan(codigo):
            print("Plan eliminado")
            print(planes)
            print(inscripciones)
        else:
            print("El codigo no existe")

    elif menu == 6:
        limpiar()
        print("programa finalizado.")
        break
    else:
        print("Debe seleccionar una opción válida")




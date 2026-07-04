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
        tipo = input("Ingrese tipo de plan a consultar:").lower()
        cupos_tipo(tipo)
    elif menu == 2:
        print("Menu 2")
    elif menu == 3:
        print("menu 3")
    elif menu == 4:
        print("Menu 4")
    elif menu == 5:
        print("Menu 5")
    elif menu == 6:
        limpiar()
        print("programa finalizado.")
        break
    else:
        print("Debe seleccionar una opción válida")




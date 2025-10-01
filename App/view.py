import sys
import App.logic as lg
import DataStructures.single_linked as ll


def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    pass

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    catalog = new_logic()
    catalog = lg.load_data(catalog)
    return catalog


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    print(lg.get_data(control, id))

def print_req_1(data, date_min, date_max, num):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    info = lg.req_1(data, date_min, date_max, num)
    if len(info) == 3:
        final_list, num, time = info
        print(f"\nTiempo de ejecución: {time} ms")
        print(f"Número total de trayectos en la franja: {ll.size(final_list)}")
        print(f"\nLos {num} primeros trayectos en la franja son:")
        for i in range(num):
            print(ll.get_element(final_list, i))
        print(f"\nLos {num} últimos trayectos en la franja son:")
        for i in range(ll.size(final_list) - num, ll.size(final_list)):
            print(ll.get_element(final_list, i))
    else:
        final_list_1, final_list_2, total, time = info
        print(f"\nTiempo de ejecución: {time} ms")
        print(f"Número total de trayectos en la franja: {total}")
        print(f"\nLos {num} primeros trayectos en la franja son:")
        for i in range(num):
            print(ll.get_element(final_list_1, i))
        print(f"\nLos {num} últimos trayectos en la franja son:")
        for i in range(num):
            print(ll.get_element(final_list_2, i))


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
            print(data)
        elif int(inputs) == 1:
            print_req_1(control)
            date_min = input("Ingrese la fecha y hora inicial de la franja (formato “%Y-%m-%d %H:%M:%S” ej.: '2015-01-15 07:00:00'): ")
            date_max = input("Ingrese la fecha y hora final de la franja: ")
            num = int(input("Ingrese el tamaño de la muestra (num) de trayectos a mostrar al principio y al final de la franja: "))
            print_req_1(data, date_min, date_max, num)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 5:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)

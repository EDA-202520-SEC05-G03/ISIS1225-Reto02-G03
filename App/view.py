import sys
import App.logic as lg
import DataStructures.single_linked as ll


def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    return lg.new_logic()

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
    data = lg.load_data(catalog)
    return data


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
    date_min_int = lg.date_to_int(date_min)
    date_max_int = lg.date_to_int(date_max)
    info = lg.req_1(data, date_min_int, date_max_int, num)
    if len(info) == 3:
        print("3")
        final_list, count, time = info
        print(f"\nTiempo de ejecución: {time} ms")
        print(f"Número total de trayectos en la franja: {ll.size(final_list)}")
        print(f"\nLos {ll.size(final_list)} trayectos en la franja son:")
        for i in range(ll.size(final_list)):
            print(ll.get_element(final_list, i))
    else:
        print(len(info))
        final_list_1, final_list_2, count, time = info
        print(f"\nTiempo de ejecución: {time} ms")
        print(f"Número total de trayectos en la franja: {count}")
        print(f"\nLos {count} primeros trayectos en la franja son:")
        for i in range(count):
            print(ll.get_element(final_list_1, i))
        print(f"\nLos {count} últimos trayectos en la franja son:")
        for i in range(count):
            print(ll.get_element(final_list_2, i))


def print_req_2(data, lat_min, lat_max, num):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    info = lg.req_2(data, lat_min, lat_max, num)
    
    if len(info) == 3:
        all_list, count, time = info
        print(f"\nTiempo de ejecución: {time:.2f} ms")
        print(f"Número total de trayectos en el rango: {count}")
        print(f"\nLos {ll.size(all_list)} trayectos dentro del rango son:")
        for i in range(ll.size(all_list)):
            print(ll.get_element(all_list, i))
    else:
        first_list, last_list, total, num, time = info
        print(f"\nTiempo de ejecución: {time:.2f} ms")
        print(f"Número total de trayectos en el rango: {total}")
        print(f"\nLos {num} primeros trayectos (mayores latitudes):")
        for i in range(num):
            print(ll.get_element(first_list, i))
        print(f"\nLos {num} últimos trayectos (menores latitudes dentro del rango):")
        for i in range(num):
            print(ll.get_element(last_list, i))

def print_req_3(data, dist_min, dist_max, num):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # Ejecutar la lógica del requerimiento 3
    info = lg.req_3(data, dist_min, dist_max, num)

    if len(info) == 3:
        all_list, count, time = info
        print(f"\nTiempo de ejecución: {time:.2f} ms")
        print(f"Número total de trayectos en el rango: {count}")
        print(f"\nLos {ll.size(all_list)} trayectos dentro del rango son:")
        for i in range(ll.size(all_list)):
            print(ll.get_element(all_list, i))

    else:
        first_list, last_list, total, num, time = info
        print(f"\nTiempo de ejecución: {time:.2f} ms")
        print(f"Número total de trayectos en el rango: {total}")
        print(f"\nLos {num} primeros trayectos (mayores distancias):")
        for i in range(num):
            print(ll.get_element(first_list, i))
        print(f"\nLos {num} últimos trayectos (menores distancias dentro del rango):")
        for i in range(num):
            print(ll.get_element(last_list, i))
    


def print_req_4(data, date, time, flag, num):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    ranked_list, count, ex_time = lg.req_4(data, date, time, flag)
    print(f"\nLos {num} primeros trayectos ({time}, {date})")
    for i in range(num):
        print(ll.get_element(ranked_list, i))
    print(f"\nLos {num} últimos trayectos ({time}, {date})")
    for i in range(num):
        print(ll.get_element(ranked_list, ll.size(ranked_list) - num + i))    
    print(f"\nTiempo de ejecución:{ex_time} ms")
    print(f"Número total de barrios con al menos {ll.size(ranked_list)} viajes iniciados a esa hora: {count}")

def print_req_5(data, fecha_hora, n):

    """
        Función que imprime la solución del Requerimiento 5 en consola.
        - fecha_hora: 'YYYY-MM-DD HH' (ej. '2015-01-15 08')
        - n: tamaño de la muestra
    """
    resultado = lg.req_5(data, fecha_hora, n)

    if len(resultado) == 3:
        lista_todos, total, tiempo = resultado
        print(f"\nTiempo de ejecución: {tiempo:.2f} ms")
        print(f"Fecha/Hora de terminación: {fecha_hora}")
        print(f"Total de trayectos encontrados: {total}")

        if total == 0:
            print("\nNo se encontraron trayectos que cumplan el filtro.")
        else:
            print(f"\nSe listan todos los {total} trayectos (≤ 2N):\n")
            for i in range(ll.size(lista_todos)):
                viaje = ll.get_element(lista_todos, i)
                print(f"  Recogida: {viaje[0]}  |  Pos: [{viaje[1][0]}, {viaje[1][1]}]")
                print(f"  Dejada:   {viaje[2]}  |  Pos: [{viaje[3][0]}, {viaje[3][1]}]")
                print(f"  Distancia: {viaje[4]} mi  |  Total: ${viaje[5]}\n")

    else:
        primeros, ultimos, total, n_devuelto, tiempo = resultado
        print(f"\nTiempo de ejecución: {tiempo:.2f} ms")
        print(f"Fecha/Hora de terminación: {fecha_hora}")
        print(f"Total de trayectos encontrados: {total}")

        print(f"\nPrimeros {n_devuelto} (más recientes → más antiguos):\n")
        for i in range(ll.size(primeros)):
            viaje = ll.get_element(primeros, i)
            print(f"  Recogida: {viaje[0]}  |  Pos: [{viaje[1][0]}, {viaje[1][1]}]")
            print(f"  Dejada:   {viaje[2]}  |  Pos: [{viaje[3][0]}, {viaje[3][1]}]")
            print(f"  Distancia: {viaje[4]} mi  |  Total: ${viaje[5]}\n")

        print(f"\nÚltimos {n_devuelto} (más recientes → más antiguos):\n")
        for i in range(ll.size(ultimos)):
            viaje = ll.get_element(ultimos, i)
            print(f"  Recogida: {viaje[0]}  |  Pos: [{viaje[1][0]}, {viaje[1][1]}]")
            print(f"  Dejada:   {viaje[2]}  |  Pos: [{viaje[3][0]}, {viaje[3][1]}]")
            print(f"  Distancia: {viaje[4]} mi  |  Total: ${viaje[5]}\n")


def print_req_6(data, barrio, hora_ini, hora_fin, n):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    
    resultado = lg.requerimiento_6(data, barrio, hora_ini, hora_fin, n)

    # Caso 1: retorna (todos, total, tiempo)
    if len(resultado) == 3:
        lista_todos, total, tiempo = resultado
        print(f"\nTiempo de ejecución: {tiempo:.2f} ms")
        print(f"Barrio: {barrio}  |  Rango de horas: {hora_ini}-{hora_fin}")
        print(f"Total de trayectos encontrados: {total}")

        if total == 0:
            print("\nNo se encontraron trayectos que cumplan el filtro.")
        else:
            print(f"\nSe listan todos los {total} trayectos (menos de 2N):\n")
            for i in range(ll.size(lista_todos)):
                viaje = ll.get_element(lista_todos, i)
                print(f"  Recogida: {viaje[0]}  |  Pos: [{viaje[1][0]}, {viaje[1][1]}]")
                print(f"  Dejada:   {viaje[2]}  |  Pos: [{viaje[3][0]}, {viaje[3][1]}]")
                print(f"  Distancia: {viaje[4]} mi  |  Total: ${viaje[5]}\n")

    # Caso 2: retorna (primeros, ultimos, total, n, tiempo)
    else:
        primeros, ultimos, total, n_devuelto, tiempo = resultado
        print(f"\nTiempo de ejecución: {tiempo:.2f} ms")
        print(f"Barrio: {barrio}  |  Rango de horas: {hora_ini}-{hora_fin}")
        print(f"Total de trayectos encontrados: {total}")

        print(f"\nPrimeros {n_devuelto} trayectos (más antiguos → más recientes):\n")
        for i in range(ll.size(primeros)):
            viaje = ll.get_element(primeros, i)
            print(f"  Recogida: {viaje[0]}  |  Pos: [{viaje[1][0]}, {viaje[1][1]}]")
            print(f"  Dejada:   {viaje[2]}  |  Pos: [{viaje[3][0]}, {viaje[3][1]}]")
            print(f"  Distancia: {viaje[4]} mi  |  Total: ${viaje[5]}\n")

        print(f"\nÚltimos {n_devuelto} trayectos (más antiguos → más recientes):\n")
        for i in range(ll.size(ultimos)):
            viaje = ll.get_element(ultimos, i)
            print(f"  Recogida: {viaje[0]}  |  Pos: [{viaje[1][0]}, {viaje[1][1]}]")
            print(f"  Dejada:   {viaje[2]}  |  Pos: [{viaje[3][0]}, {viaje[3][1]}]")
            print(f"  Distancia: {viaje[4]} mi  |  Total: ${viaje[5]}\n")

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
            date_min = "2015-01-07 22:08:47" #input("Ingrese la fecha y hora inicial de la franja (formato “%Y-%m-%d %H:%M:%S” ej.: '2015-01-15 07:00:00'): ")
            date_max = "2015-01-25 22:06:47" #input("Ingrese la fecha y hora final de la franja: ")
            num = int(input("Ingrese el tamaño de la muestra (num) de trayectos a mostrar al principio y al final de la franja: "))
            print_req_1(data, date_min, date_max, num)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            dist_min = float(input("Distancia mínima (mi): ").strip())
            dist_max = float(input("Distancia máxima (mi): ").strip())
            num = int(input("Tamaño de la muestra (N): ").strip())
            print_req_3(control, dist_min, dist_max, num)

        elif int(inputs) == 4:
            date = "2015-01-15" #input("Ingrese la fecha (formato “%Y-%m-%d” ej.: '2015-01-15'): ")
            time = "17:00:00" #input("Ingrese la hora (formato “%H:%M:%S” ej.: '07:00:00'): ")
            flag = bool(int(input("Ingrese 1 si desea ver los 5 barrios con más viajes iniciados a esa hora, o 0 si desea ver los 5 barrios con más viajes terminados a esa hora: ")))
            num = int(input("Ingrese el número de viajes mínimos que debe tener un barrio para ser considerado en el ranking: "))
            print_req_4(data, date, time, flag, num)

        elif int(inputs) == 5:
            fecha_hora = input("Fecha y hora de terminación (YYYY-MM-DD HH, ej. '2015-01-15 08'): ").strip()
            n = int(input("Tamaño de la muestra (N): ").strip())
            print_req_5(data, fecha_hora, n)

        elif int(inputs) == 6:
            barrio = input("Barrio de recogida (ej. 'Midtown'): ").strip()
            hora_ini = input("Hora inicial (HH, ej. '09'): ").strip()
            hora_fin = input("Hora final (HH, ej. '12'): ").strip()
            n = int(input("Tamaño de la muestra (N): ").strip())
            print_req_6(data, barrio, hora_ini, hora_fin, n)
           

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)

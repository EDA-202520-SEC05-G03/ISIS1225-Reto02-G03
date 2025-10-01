import time
import csv
import os
from DataStructures import array_list as lt
from DataStructures import single_linked_list as ll
import math
from DataStructures import array_list as lt

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'
csv.field_size_limit(2147483647)

def get_time():
    """Retorna el tiempo actual en milisegundos"""
    return float(time.perf_counter() * 1000)

def delta_time(start, end):
    """Calcula la diferencia de tiempo en milisegundos"""
    return end - start


def new_logic():
    """
    Crea el catálogo para almacenar las estructuras de datos
    """
    catalog = {
        'trips': lt.new_list(),
        'neighborhoods': lt.new_list(),
    }
    return catalog


# Funciones para la carga de datos

def load_data(catalog):
    """
    Carga los datos del reto
    """
    # Cargar taxis
    file = data_dir + 'taxis-small.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    for record in input_file:
        lt.add_last(catalog['trips'], record)

    # Cargar vecindarios
    file = data_dir + 'nyc-neighborhoods.csv'  
    input_file = csv.DictReader(open(file, encoding='utf-8'))  
    for neighborhood in input_file:
        lt.add_last(catalog['neighborhoods'], neighborhood)

    return catalog

# Funciones de consulta sobre el catálogo

def date_to_int(date_str):
    """
    Convierte una fecha en formato string a un entero para facilitar comparaciones.
    Formato esperado: 'YYYY-MM-DD HH:MM:SS'
    """
    date_clean = date_str.replace(" ", "").replace("-", "").replace(":", "")
    return int(date_clean)

def info_req1(record):
    """
    Extrae la información relevante para el requerimiento 1 de un registro de viaje.
    """
    date_pickup = record["pickup_datetime"]
    date_dropoff = record["dropoff_datetime"]
    lat_pickup = float(record["pickup_latitude"])
    lon_pickup = float(record["pickup_longitude"])
    lat_dropoff = float(record["dropoff_latitude"])
    lon_dropoff = float(record["dropoff_longitude"])
    distance = float(record["trip_distance"])
    total_cost = float(record["total_amount"])
    return (date_pickup, [lat_pickup, lon_pickup], date_dropoff, [lat_dropoff, lon_dropoff], distance, total_cost)

def req_1(catalog, date_min, date_max, num):
    """
    Los trayectos en una franja fecha y tiempo de recogida ordenados del más antiguo al más reciente
    Args:
    • Fecha y tiempo inicial de la franja (formato “%Y-%m-%d %H:%M:%S” ej.: "2015-01-15 07:00:00").
    • Fecha y tiempo final de la franja (formato “%Y-%m-%d %H:%M:%S” ej.: "2015-01-15 08:30:00").
    • Tamaño de la muestra (num) de trayectos a mostrar al principio y al final de la franja
    Retorna:
    • Tiempo de la ejecución del requerimiento en milisegundos.
    • Número total de trayectos que cumplieron el filtro de fecha y hora de recogida.
    • Mostrar la siguiente información de cada uno de los N primeros trayectos y de los N últimos trayectos
    de la franja:
        - Fecha y tiempo de recogida (formato AAAA-MM-DD HH:MM:SS) * criterio de ordenamiento
        - Latitud y longitud de recogida (formato [Latitud, Longitud])
        - Fecha y tiempo de terminación (formato AAAA-MM-DD HH:MM:SS)
        - Latitud y longitud de terminación (formato [Latitud, Longitud])
        - Distancia recorrida (millas)
        - Costo total pagado
    """
    a = get_time()
    trips = ll.new_list()
    
    for index in range(lt.size(catalog["trips"])):
        record = lt.get_element(catalog["trips"], index)
        date_pickup = date_to_int(record["pickup_datetime"])
        date_dropoff = date_to_int(record["dropoff_datetime"])
        if date_pickup >= date_min and date_dropoff <= date_max:
            ll.add_last(trips, record)
    
    # Sort the trips by date (change to a more efficient sorting algorithm if needed)
    for i in range(ll.size(trips) - 1):
        for j in range(i+1, ll.size(trips)):
            date_i = date_to_int(ll.get_element(trips, i)["pickup_datetime"])
            date_j = date_to_int(ll.get_element(trips, j)["pickup_datetime"])
            if date_i > date_j:
                temp = ll.get_element(trips, i)
                trips["elements"][i] = ll.get_element(trips, j)
                trips["elements"][j] = temp
    
    final_list_1 = ll.new_list()
    final_list_2 = ll.new_list()
    if ll.size(trips) > 2 * num:
        for i in range(num):
            record = ll.get_element(trips, i)
            ll.add_last(final_list_1, info_req1(record))
            record = ll.get_element(trips, ll.size(trips) - 1 - i)
            ll.add_last(final_list_2, info_req1(record))
            b = get_time()
            time = delta_time(a, b)
        return (final_list_1, final_list_2, ll.size(trips), time)
    else:
        final_list = ll.new_list()
        for i in range(ll.size(trips)):
            record = ll.get_element(trips, i)
            ll.add_last(final_list, info_req1(record))
            b = get_time()
            time = delta_time(a, b)
    return (final_list, num, time)

def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

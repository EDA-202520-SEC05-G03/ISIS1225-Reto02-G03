import time
import csv
import os
from DataStructures import array_list as lt
from DataStructures import single_linked as ll
import math
from DataStructures import array_list as lt
from DataStructures import map as mp

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

def compare_dates(record_1, record_2):
    date_1 = record_1["pickup_datetime"]
    date_2 = record_2["pickup_datetime"]
    if date_1 < date_2:
        return 0
    elif date_1 > date_2:
        return 1
    else:
        return -1

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
            
    # Sort the trips by date
    ll.sort(trips, compare_dates)
            
    size = ll.size(trips)
    if size > 2 * num:
        final_list_1 = ll.new_list()
        final_list_2 = ll.new_list()
        for i in range(num):
            record = ll.get_element(trips, i)
            ll.add_last(final_list_1, info_req1(record))
            record = ll.get_element(trips, size - 1 - i)
            ll.add_last(final_list_2, info_req1(record))
        b = get_time()
        time = delta_time(a, b)
        return (final_list_1, final_list_2, num, time)
    else:
        final_list = ll.new_list()
        for i in range(size):
            record = ll.get_element(trips, i)
            ll.add_last(final_list, info_req1(record))
        b = get_time()
        time = delta_time(a, b)
        return (final_list, size, time)

def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass

def info_req3(record):
    
    date_pickup = record["pickup_datetime"]
    date_dropoff = record["dropoff_datetime"]
    lat_pickup = float(record["pickup_latitude"])
    lon_pickup = float(record["pickup_longitude"])
    lat_dropoff = float(record["dropoff_latitude"])
    lon_dropoff = float(record["dropoff_longitude"])
    distance = float(record["trip_distance"])
    total_cost = float(record["total_amount"])
    return (date_pickup, [lat_pickup, lon_pickup], date_dropoff, [lat_dropoff, lon_dropoff], distance, total_cost)


def req_3(catalog, dist_min, dist_max, num):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start = get_time()
    filtered = ll.new_list()

    total = lt.size(catalog["trips"])
    for i in range(total):
        rec = lt.get_element(catalog["trips"], i)
        dist = float(rec["trip_distance"])
        if dist_min <= dist <= dist_max:
            ll.add_last(filtered, rec)

    ll.sort(filtered, compare_distance_desc)

    size = ll.size(filtered)
    if size > 2 * num:
        first_list = ll.new_list()
        last_list = ll.new_list()
        for i in range(num):
            r1 = ll.get_element(filtered, i)
            ll.add_last(first_list, info_req3(r1))
            r2 = ll.get_element(filtered, size - 1 - i)
            ll.add_last(last_list, info_req3(r2))
        end = get_time()
        return (first_list, last_list, size, num, delta_time(start, end))
    else:
        all_list = ll.new_list()
        for i in range(size):
            r = ll.get_element(filtered, i)
            ll.add_last(all_list, info_req3(r))
        end = get_time()
        return (all_list, size, delta_time(start, end))

# Funciones auxiliares

def get_date(date_str):
    """
    Extrae la fecha (YYYY-MM-DD) de un string de fecha y hora (YYYY-MM-DD HH:MM:SS)
    """
    return int(date_str[:10])

def build_pickup_index(catalog):
    """
    Builds a HashMap where:
      - Key = pickup date (YYYY-MM-DD)
      - Value = list of trips that start on that date
    This allows fast access to trips by pickup date.
    """
    pickup_map = mp.new_map(2000)  # Set size properly

    for record in lt.iterator(catalog["trips"]):
        # Extract only the date part (YYYY-MM-DD) from pickup datetime
        dropoff_date = date_to_int(record["dropoff_datetime"][:10])

        # If date is not yet in the map, create a new entry
        if not mp.contains(pickup_map, dropoff_date):
            mp.put(pickup_map, dropoff_date, lt.new_list())

        # Append this trip to the list of trips for that date
        entry = mp.get(pickup_map, dropoff_date)
        lt.add_last(entry["value"], record)

    return pickup_map


def build_dropoff_index(catalog):
    """
    Construye un índice hash por fecha de terminación (YYYY-MM-DD).
    Cada llave es una fecha y el valor asociado es una lista de viajes.
    """
    dropoff_map = mp.new_map()
    for trip in lt.iterator(catalog["trips"]):
        drop_date = trip["dropoff_datetime"][:10]  # 'YYYY-MM-DD'
        if mp.contains(dropoff_map, drop_date):
            entry = mp.get(dropoff_map, drop_date)["value"]
            if entry is None:
                entry = lt.new_list()
            else:
                ll.add_last(entry, trip)
        else:
            new_list = ll.new_list()
            ll.add_last(new_list, trip)
            mp.put(dropoff_map, drop_date, new_list)
    return dropoff_map


def req_4(data, date_str, time_str, flag):
    """
    Requerimiento 4 usando hashmap:
    - flag = True → "ANTES"
    - flag = False → "DESPUES"
    """
    a = get_time()

    dropoff_map = build_dropoff_index(data)
    print()
    print(dropoff_map)
    print()
    print(date_str)
    if not mp.contains(dropoff_map, date_str):
        return (ll.new_list(), 0, 0)

    trips_on_date = mp.get(dropoff_map, date_str)["value"]

    time_int = date_to_int(time_str)  # se reusa date_to_int
    filtered = ll.new_list()

    for trip in ll.iterator(trips_on_date):
        print("erm")
        drop_int = date_to_int(trip["dropoff_datetime"][11:19])  # HH:MM:SS
        if flag and drop_int < time_int:      # ANTES
            ll.add_last(filtered, trip)
        elif not flag and drop_int > time_int:  # DESPUES
            ll.add_last(filtered, trip)

    # Ordena de más reciente a más antiguo
    ll.sort(filtered, compare_dates)

    all_list = ll.new_list()
    for trip in ll.iterator(filtered):
        ll.add_last(all_list, info_req1(trip))
    b = get_time()
    time = delta_time(a, b)
    
    print(f"Tiempo de ejecución: {time} ms")
    print(f"Número total de viajes que cumplen el criterio: {ll.size(all_list)}")
        
    return (all_list, ll.size(all_list), time)

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

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

# Funciones de consulta sobre el catálogos


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

def compare_distance_desc(record_1, record_2):
    d1 = float(record_1["trip_distance"])
    d2 = float(record_2["trip_distance"])
    if d1 > d2:
        return 0
    elif d1 < d2:
        return 1
    else:
        t1 = float(record_1["total_amount"])
        t2 = float(record_2["total_amount"])
        if t1 > t2:
            return 0
        elif t1 < t2:
            return 1
        else:
            return -1

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
    dist_min = float(dist_min)
    dist_max = float(dist_max)
    if dist_min > dist_max:
        dist_min, dist_max = dist_max, dist_min

    start = get_time()

    filtered = ll.new_list()
    for rec in lt.iterator(catalog["trips"]):
        dist = float(rec["trip_distance"])
        if dist_min <= dist <= dist_max:
            ll.add_last(filtered, rec)

    ll.sort(filtered, compare_distance_desc)

    size = ll.size(filtered)

    if size == 0:
        end = get_time()
        return (ll.new_list(), 0, delta_time(start, end))

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
        for rec in ll.iterator(filtered):
            ll.add_last(all_list, info_req3(rec))
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

def distancia_haversine(lat1, lon1, lat2, lon2):
    """
    Calcula la distancia Haversine (en millas) entre dos coordenadas geográficas.
    """
    radio_tierra = 3958.8  # en millas
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * (math.sin(dlon / 2) ** 2)
    c = 2 * math.asin(math.sqrt(a))
    return radio_tierra * c


def obtener_hora(fecha_hora):
    """
    Extrae la hora (HH) de una cadena con formato 'YYYY-MM-DD HH:MM:SS'.
    """
    return int(fecha_hora[11:13])


def barrio_mas_cercano(lista_barrios, lat, lon):
    """
    Retorna el nombre del barrio más cercano a una coordenada (lat, lon),
    usando la distancia Haversine.
    """
    distancia_minima = None
    barrio_cercano = None

    for barrio in lt.iterator(lista_barrios):
        lat_barrio = float(barrio["latitude"])
        lon_barrio = float(barrio["longitude"])
        distancia = distancia_haversine(lat, lon, lat_barrio, lon_barrio)

        if distancia_minima is None or distancia < distancia_minima:
            distancia_minima = distancia
            barrio_cercano = barrio["neighborhood"]

    return barrio_cercano


def crear_mapa_barrios(catalogo):
    """
    Crea un mapa hash donde la llave es el nombre del barrio
    y el valor es una lista con los trayectos de ese barrio.
    """
    mapa_barrios = mp.new_map()
    lista_barrios = catalogo["neighborhoods"]

    for trayecto in lt.iterator(catalogo["trips"]):
        lat = float(trayecto["pickup_latitude"])
        lon = float(trayecto["pickup_longitude"])
        nombre_barrio = barrio_mas_cercano(lista_barrios, lat, lon)

        if mp.contains(mapa_barrios, nombre_barrio):
            lista_trayectos = mp.get(mapa_barrios, nombre_barrio)["value"]
            ll.add_last(lista_trayectos, trayecto)
        else:
            nueva_lista = ll.new_list()
            ll.add_last(nueva_lista, trayecto)
            mp.put(mapa_barrios, nombre_barrio, nueva_lista)

    catalogo["indice_barrios"] = mapa_barrios
    return mapa_barrios


def comparar_por_fecha_recogida(viaje1, viaje2):
    """
    Compara dos viajes por fecha de recogida (pickup_datetime)
    para orden ascendente 
    """
    f1 = viaje1["pickup_datetime"]
    f2 = viaje2["pickup_datetime"]
    if f1 < f2:
        return 0
    elif f1 > f2:
        return 1
    else:
        return -1


def info_requerimiento6(viaje):
    """
    Retorna la información relevante de un viaje para el req 6, que es la misma que el req 1.
    """
    return info_req1(viaje)


def requerimiento_6(catalogo, nombre_barrio, hora_inicio, hora_fin, cantidad):
    """
    Retorna los trayectos recogidos en un barrio dentro de un rango de horas.
    """
    hora_inicio = int(hora_inicio)
    hora_fin = int(hora_fin)

    if hora_inicio > hora_fin:
        temp = hora_inicio
        hora_inicio = hora_fin
        hora_fin = temp

    inicio = get_time()

   
    if "indice_barrios" in catalogo:
        mapa_barrios = catalogo["indice_barrios"]
    else:
        mapa_barrios = crear_mapa_barrios(catalogo)

    if not mp.contains(mapa_barrios, nombre_barrio):
        fin = get_time()
        return (ll.new_list(), 0, delta_time(inicio, fin))

    lista_barrio = mp.get(mapa_barrios, nombre_barrio)["value"]

    lista_filtrada = ll.new_list()
    for trayecto in ll.iterator(lista_barrio):
        hora = obtener_hora(trayecto["pickup_datetime"])
        if hora >= hora_inicio and hora <= hora_fin:
            ll.add_last(lista_filtrada, trayecto)

    ll.sort(lista_filtrada, comparar_por_fecha_recogida)

    total = ll.size(lista_filtrada)

    if total == 0:
        fin = get_time()
        return (ll.new_list(), 0, delta_time(inicio, fin))

    if total > 2 * cantidad:
        primeros = ll.new_list()
        ultimos = ll.new_list()

        for i in range(cantidad):
            viaje1 = ll.get_element(lista_filtrada, i)
            ll.add_last(primeros, info_requerimiento6(viaje1))
            viaje2 = ll.get_element(lista_filtrada, total - 1 - i)
            ll.add_last(ultimos, info_requerimiento6(viaje2))

        fin = get_time()
        return (primeros, ultimos, total, cantidad, delta_time(inicio, fin))
    else:
        todos = ll.new_list()
        for trayecto in ll.iterator(lista_filtrada):
            ll.add_last(todos, info_requerimiento6(trayecto))

        fin = get_time()
        return (todos, total, delta_time(inicio, fin))



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

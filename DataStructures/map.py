# import python modules
import random as rd
from DataStructures import array_list as lt
from DataStructures import entry as me
from DataStructures import numbers as num
from App import logic as lg


def default_mp_entry_cmp(key, entry) -> int:
    if (key == entry["key"]):
        return 0
    elif (key > entry["key"]):
        return 1
    return -1

def is_available(table: dict, _slot: int) -> bool:
    entry = lt.get_element(table, _slot)
    if entry["key"] is None or entry["key"] == "__EMPTY__":
        return True
    return False

def find_slot(mp: dict, key, _idx: int) -> int:
    _table = mp["table"]
    _cmp = mp["cmp_function"]
    _slot = 0
    _available_slot = -1
    while _slot != _idx:
        if _slot == 0:
            _slot = _idx
        if is_available(_table, _slot):
            entry = lt.get_element(_table, _slot)
            if _available_slot == -1:
                _available_slot = _slot
            if entry["key"] is None:
                break
        else:
            entry = lt.get_element(_table, _slot)
            if _cmp(key, entry) == 0:
                return _slot
        _slot = ((_slot % mp["capacity"]) + 1)
    return -(_available_slot)


def new_map(entries: int = 17, prime: int = 109345121, alpha: float = 0.5, key: str = None, rehashable: bool = True) -> dict:
    capacity = num.next_prime(entries // alpha)
    scale = rd.randint(1, prime - 1)
    shift = rd.randint(0, prime - 1)
    new_table = dict(
    entries=entries,
    prime=prime,
    max_alpha=alpha,
    cur_alpha=0,
    capacity=capacity,
    scale=scale,
    shift=shift,
    table=None,
    rehashable=rehashable,
    size=0,
    type="LINEAR_PROBING",
    cmp_function=default_mp_entry_cmp,
    key=key
    )
        
    new_table["table"] = lt.new_list()
    i = 0
    while i < capacity:
        entry = me.new_map_entry(None, None)
        lt.add_last(new_table["table"], entry)
        i += 1
    return new_table

def rehash(mp: dict) -> None:
    if mp["rehashable"] is True:
            _new_capacity = num.next_prime(mp["capacity"] * 2)
            _new_table = lt.new_list(mp["key"])
            i = 0
            while i < _new_capacity:
                entry = me.new_map_entry(None, None)
                lt.add_last(_new_table, entry)
                i += 1
            mp["capacity"] = _new_capacity
            mp["table"] = _new_table
            _idx = 0
            while _idx < lt.size(mp["table"]):
                entry = lt.get_element(mp["table"], _idx)
                if entry["key"] not in (None, "__EMPTY__"):
                    _idx = num.hash_compress(entry["key"], mp["scale"], mp["shift"], mp["prime"], _new_capacity)
                    _slot = find_slot(mp, entry["key"], _idx)
                    lt.update(_new_table, abs(_slot), entry)
                _idx += 1
    return mp

def put(mp: dict, key, value) -> None:
    entry = me.new_map_entry(key, value)
    _idx = num.hash_compress(key, mp["scale"], mp["shift"], mp["prime"], mp["capacity"])
    slot = find_slot(mp, key, _idx)
    # arlt.update(mp["table"], slot, entry)
    lt.update(mp["table"], abs(slot), entry)
    if slot < 0:
        mp["size"] += 1
        mp["cur_alpha"] = mp["size"] / mp["capacity"]

    if mp["cur_alpha"] >= mp["max_alpha"]:
        rehash(mp)


def get(mp: dict, key) -> dict:
    entry = None
    _idx = num.hash_compress(key, mp["scale"], mp["shift"], mp["prime"], mp["capacity"])
    _slot = find_slot(mp, key, _idx)
    if _slot > 0:
        entry = lt.get_element(mp["table"], _slot)
    return entry


def remove(mp: dict, key) -> dict:
    _idx = num.hash_compress(key, mp["scale"], mp["shift"], mp["prime"], mp["capacity"])
    _slot = find_slot(mp, key, _idx)
    if _slot > -1:
        dummy = me.new_map_entry("__EMPTY__", "__EMPTY__")
        lt.update(mp["table"], _slot, dummy)
        mp["size"] -= 1
    return mp

def size(mp: dict) -> int:
    return mp.get("size")

def contains(mp: dict, key) -> bool:
    _idx = num.hash_compress(key, mp["scale"], mp["shift"], mp["prime"], mp["capacity"])
    _slot = find_slot(mp, key, _idx)
    if _slot > 0:
        return True
    return False
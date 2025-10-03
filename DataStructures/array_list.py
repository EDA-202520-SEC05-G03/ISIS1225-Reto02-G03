def dflt_elm_cmp_lt(id1, id2) -> int:
    if id1 > id2:
        return 1
    elif id1 < id2:
        return -1
    return 0

def new_list(key: str = "id"):
    new_lt = dict(
        elements=[],
        size = 0,
        type="ARRAYLIST",
        cmp_function = dflt_elm_cmp_lt,
    )
    return new_lt

def size(lst):
    return lst.get("size")

def is_empty(lst):
    return lst["size"] == 0

def get_element(lst, index):
    if 0 <= index < lst["size"]:
        return lst["elements"][index]
    return None

def is_present(lst, element, cmp_function=None):
    cmp_function = cmp_function or lst["cmp_function"]
    for i, info in enumerate(lst["elements"]):
        if cmp_function(element, info) == 0:
            return i
    return -1

def first_element(lst):
    if lst["size"] > 0:
        return lst["elements"][0]
    return None

def last_element(lst):
    if lst["size"] > 0:
        return lst["elements"][-1]
    return None

def add_first(lst, element):
    lst["elements"].insert(0, element)
    lst["size"] += 1

def add_last(lst, element):
    lst["elements"].append(element)
    lst["size"] += 1

def insert_element(lst, index, element):
    if 0 <= index <= lst["size"]:
        lst["elements"].insert(index, element)
        lst["size"] += 1
        return True
    return False

def change_info(lst, old_element, new_element):
    index = is_present(lst, old_element)
    if index != -1:
        lst["elements"][index] = new_element
        return True
    return False

def iterator(lst):
    for pos in range(lst["size"]):
        yield lst["elements"][pos]
        
def exchange(lst, pos1, pos2):
    if 0 <= pos1 < lst["size"] and 0 <= pos2 < lst["size"]:
        lst["elements"][pos1], lst["elements"][pos2] = lst["elements"][pos2], lst["elements"][pos1]
        return True
    return False        
        
def sort(lst, sort_crit) :
        size = lst["size"]
        pos1 = 1
        while pos1 <= size:
            pos2 = pos1
            while (pos2 > 1) and sort_crit(get_element(lst, pos2), get_element(lst, pos2-1)) :
                exchange(lst, pos2, pos2-1)
                pos2 -= 1
            pos1 += 1
        return lst     

def update(lst: dict, pos: int, element) -> None:
    lst["elements"][pos] = element   
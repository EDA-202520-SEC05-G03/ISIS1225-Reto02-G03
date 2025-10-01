def dflt_elm_cmp_lt(id1, id2) -> int:
    if id1 > id2:
        return 1
    elif id1 < id2:
        return -1
    return 0

def new_list(cmp_function, key: str = "id"):
    new_lt = dict(
        elements=[],
        size=0,
        type="ARRAYLIST",
        cmp_function=cmp_function or dflt_elm_cmp_lt,
        key=key,
    )
    return new_lt

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

def size(lst):
    return lst["size"]

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

def iterator(lst: dict):
    for pos in range(lst["size"]):
        yield lst["elements"][pos]
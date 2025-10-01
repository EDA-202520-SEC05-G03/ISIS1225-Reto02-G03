def dflt_elm_cmp_lt(id1, id2) -> int:
    if id1 > id2:
        return 1
    elif id1 < id2:
        return -1
    return 0

def new_single_node(data):
    node = {
        "data": data,
        "next": None
    }
    return node

def new_list(cmp_function=None, key: str = "id"):
    return {
        "first": None,
        "last": None,
        "size": 0,
        "type": "SINGLELINKED",
        "cmp_function": cmp_function or dflt_elm_cmp_lt,
        "key": key,
    }

def get_element(lst, pos):
    if pos < 0 or pos >= lst["size"]:
        return None
    idx = 0
    cur = lst["first"]
    while idx < pos:
        cur = cur["next"]
        idx += 1
    return cur["data"]

def add_first(lst, element):
    new_node = new_single_node(element)
    new_node["next"] = lst["first"]
    lst["first"] = new_node
    if lst["size"] == 0:
        lst["last"] = new_node
    lst["size"] += 1

def add_last(lst, element):
    new_node = new_single_node(element)
    if lst["size"] == 0:
        lst["first"] = new_node
    else:
        lst["last"]["next"] = new_node
    lst["last"] = new_node
    lst["size"] += 1    

def first_element(lst):
    return lst["first"]["data"] if lst["first"] else None

def last_element(lst):
    return lst["last"]["data"] if lst["last"] else None

def size(lst):
    return lst["size"]

def is_empty(lst):
    return lst["size"] == 0

def remove_element(lst, pos):
    if pos < 0 or pos >= lst["size"]:
        return None
    cur = lst["first"]
    if pos == 0:
        lst["first"] = cur["next"]
        if lst["size"] == 1:
            lst["last"] = None
    else:
        prev = None
        idx = 0
        while idx < pos:
            prev = cur
            cur = cur["next"]
            idx += 1
        prev["next"] = cur["next"]
        if cur == lst["last"]:
            lst["last"] = prev
    lst["size"] -= 1
    return cur["data"]

def remove_first(lst):
    return remove_element(lst, 0)

def remove_last(lst):
    return remove_element(lst, lst["size"] - 1)

def insert_element(lst, element, pos):
    if pos < 0 or pos > lst["size"]:
        return False
    new_node = new_single_node(element)
    if pos == 0:
        new_node["next"] = lst["first"]
        lst["first"] = new_node
        if lst["size"] == 0:
            lst["last"] = new_node
    else:
        prev = None
        cur = lst["first"]
        idx = 0
        while idx < pos:
            prev = cur
            cur = cur["next"]
            idx += 1
        new_node["next"] = cur
        prev["next"] = new_node
        if cur is None:  # inserted at the end
            lst["last"] = new_node
    lst["size"] += 1
    return True

def iterator(lst):
    cur = lst["first"]
    while cur:
        yield cur["data"]
        cur = cur["next"]
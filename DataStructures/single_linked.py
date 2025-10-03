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
    if is_not_empty(lst):
        lst["last"] = new_node
    lst["size"] += 1

def add_last(lst, element):
    new_node = new_single_node(element)
    if is_not_empty(lst):
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
    return lst.get("size")

def is_not_empty(lst):
    return size(lst) == 0

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
        
def switch_elements(lst, pos1, pos2):
    if pos1 < 0 or pos1 >= lst["size"] or pos2 < 0 or pos2 >= lst["size"] or pos1 == pos2:
        return False
    if pos1 > pos2:
        pos1, pos2 = pos2, pos1
    prev1 = None
    cur1 = lst["first"]
    idx = 0
    while idx < pos1:
        prev1 = cur1
        cur1 = cur1["next"]
        idx += 1
    prev2 = prev1
    cur2 = cur1
    while idx < pos2:
        prev2 = cur2
        cur2 = cur2["next"]
        idx += 1
    if prev1:
        prev1["next"] = cur2
    else:
        lst["first"] = cur2
    if prev2 != cur1:
        prev2["next"] = cur1
    else:
        prev2 = cur1
    temp = cur1["next"]
    cur1["next"] = cur2["next"]
    cur2["next"] = temp
    if cur1["next"] is None:
        lst["last"] = cur1
    if cur2["next"] is None:
        lst["last"] = cur2
    return True

def sort(lst, sort_crit, reverse=False):
    size = lst["size"]
    pos1 = 1
    while pos1 <= size:
        pos2 = pos1
        while pos2 > 1:
            cmp = sort_crit(get_element(lst, pos2 - 1), get_element(lst, pos2 - 2))
            if (not reverse and cmp < 0) or (reverse and cmp > 0):
                switch_elements(lst, pos2 - 1, pos2 - 2)
                pos2 -= 1
            else:
                break
        pos1 += 1
    return lst
   
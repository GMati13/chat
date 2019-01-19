__storage = {}

def set_item(name, data):
    __storage[name] = data

def get_item(name):
    return __storage[name] if name in __storage else None

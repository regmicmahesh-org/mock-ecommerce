import json

_items = None
_totalDB = None
_users = None

count = 100

with open("db.json", "r") as dbFile:
    _totalDB = json.load(dbFile)
    _items = _totalDB["items"]
    _users = _totalDB["users"]


def get_by_id(id: int):
    filtered_item = next(filter(lambda x: x['id'] == id, _items), None)
    return filtered_item

def get_all():
    return _items

def add_by_id(**kwargs):
    global count
    count += 1
    _items.append({**kwargs, 'id': count})
    _totalDB["items"] = _items

def remove_one(id: int):
    global _items
    global _totalDB
    filtered_items = list(filter(lambda x: x['id'] != id, _items))
    _items = filtered_items
    _totalDB["items"] = _items
     


def login(username: str, password: str):
    global _users
    user = next(filter(lambda x: x['username'] == username and x['password'] == password, _users), None)
    return user
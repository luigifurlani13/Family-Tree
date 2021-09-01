from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

charlotte = {
    "id":5,
    "name": "Charlotte",
    "children": []
}

harrison = {
    "id":6,
    "name": "Harrison",
    "children": []
}

harry = {
    "id":4,
    "name": "Harry",
    "children": [harrison]
}

william = {
    "id":3,
    "name": "William",
    "children": [charlotte]
}

charles = {
    "id":2,
    "name": "Charles",
    "children": [william, harry]
}

queen = {
    "id":1,
    "name": "Elizabeth",
    "children": [charles]
}

members_list = []

def get_all_members(parent):
    for children in parent["children"]:
        members_list.append(children)
        get_all_members(children)
    return members_list

# print(get_all_members(queen))

def find_single_member(parent,id):
    for children in parent["children"]:
        if parent["id"] == id:
            return parent
        if children["id"] == id:
            return children
        return find_single_member(children, id)

# print(find_single_member(queen, 5))



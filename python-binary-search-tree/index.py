'''
Converted from Java 7 code @ https://www.youtube.com/watch?v=oSWTXtMglKE
'''

import jsonpickle # pip install jsonpickle
import json
import yaml # pip install pyyaml

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        '''Appends a value as a leaf to the tree. Returns without doing anything
           if the value already exists.'''
        if value == self.data:
            return
        elif value <= self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if value == self.data:
            return True
        elif value < self.data:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

n = Node(10)
n.insert(8)
n.insert(98)
n.insert(-200)
n.insert(2)
n.insert(101)
n.insert(101) # value will not get inserted since it's a duplicate

print(n.contains(2)) # True
print(n.contains(20)) # False

# https://stackoverflow.com/a/35804583/998664
print(json.dumps(json.loads(jsonpickle.encode(n)), indent=4))
'''
{
    "py/object": "__main__.Node",
    "data": 10,
    "left": {
        "py/object": "__main__.Node",
        "data": 8,
        "left": {
            "py/object": "__main__.Node",
            "data": -200,
            "left": null,
            "right": {
                "py/object": "__main__.Node",
                "data": 2,
                "left": null,
                "right": null
            }
        },
        "right": null
    },
    "right": {
        "py/object": "__main__.Node",
        "data": 98,
        "left": null,
        "right": {
            "py/object": "__main__.Node",
            "data": 101,
            "left": null,
            "right": null
        }
    }
}
'''

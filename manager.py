from typing import Any
from models import Player
import json


class Manager:
    """
    But: serealiser et deserealiser la base de donnees
    Un manager par entite
    """

    def __init__(self, item_type: Any):
        self.item_type = item_type
        item_name = item_type.__name__.lower()
        self.file = f"json\{item_name}s.json"
        self.items = {}
        with open(self.file, 'r') as data:
            data = json.loads((data.read()))
            for item_data in data:
                self.create(**item_data)

    def create(self, *args, **kwargs):
        item = self.item_type(*args, **kwargs)
        self.items[item.id] = item
        return item

    def read(self, id: int):
        return self.items[id]

    def read_all(self):
        return list(self.items.values())

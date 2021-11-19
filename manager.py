from typing import Any, Dict

from pydantic.types import PositiveFloat, PositiveInt
from models import Name, Player
import json


class Manager:
    """
    But: serealiser et deserealiser la base de donnees
    Un manager par entite
    """

    def __init__(self, item_type: Any):
        self.item_type = item_type
        self.item_name = item_type.__name__.lower()
        self.file = f"json\{self.item_name}s.json"
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
    
    def save(self, new_item: Dict):
        items = {}
        if self.item_name == 'player':
            items.update({'id': len(self.read_all()) + 1})
            items.update(new_item.copy())
            items['ranking'] = PositiveInt(items['ranking'])
            Player(id=items['id'], firstname=Name(items['firstname']), lastname=Name(items['lastname']), birthdate=items['birthdate'], gender=items['gender'], ranking=items['ranking'])
        with open(self.file, 'r+') as file:
            data = json.load(file)
            data.append(items)
            file.seek(0)
            json.dump(obj=data, fp=file, indent=4)

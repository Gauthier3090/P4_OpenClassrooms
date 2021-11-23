from typing import Any
from tinydb import TinyDB
from tinydb.table import Document
import json


class Manager:
    """
    But: serealiser et deserealiser la base de donnees
    Un manager par entite
    """

    def __init__(self, item_type: Any):
        self.item_type = item_type
        self.item_name = self.item_type.__name__.lower()
        self.items = {}
        db = TinyDB("db.json", sort_keys=True, indent=4)
        self.table = db.table(self.item_name + "s")
        self.max_id = 0
        for item_data in self.table:
            self.create(**item_data)

    def create(self, save=True, **kwargs):
        if "id" not in kwargs:
            kwargs["id"] = self.max_id + 1
        item = self.item_type(**kwargs)
        self.items[item.id] = item
        self.max_id = max(self.max_id, item.id)
        if save:
            self.save_item(item.id)
        return item

    def read(self, id: int):
        return self.items[id]

    def read_all(self):
        return list(self.items.values())

    def save_item(self, id: int):
        item = self.read(id)
        self.table.upsert(Document(json.loads(item.json()), doc_id=id))

    def update_item(self, id: str, ranking: int):
        with open('db.json', 'r+') as f:
            data = json.load(f)
            data['players'][id]['ranking'] = ranking
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

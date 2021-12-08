from pydantic import BaseModel
from pydantic.types import constr
from datetime import datetime
from typing import List
from .match import Match


class Round(BaseModel):
    name = constr(min_length=5, max_length=20)
    matches: List[Match] = []
    start_date: datetime = datetime.today()
    end_date: datetime = None

    def __str__(self):
        return f'{self.name}, {self.matches.__str__()}, {self.start_date}\
            , {self.end_date}'

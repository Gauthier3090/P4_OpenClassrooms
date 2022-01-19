from pydantic import BaseModel
from datetime import datetime
from typing import List
from pydantic.types import constr
from .match import Match


class Round(BaseModel):
    '''
        Class qui instancie les rounds d'un tournoi et qui enregistre les
        différents matchs joués ainsi que les dates de débuts et les dates de fin.
    '''
    name: constr(min_length=5, max_length=20)
    matches: List[Match] = []
    start_date: datetime = datetime.today()
    end_date: datetime = None

    def __str__(self):
        return f'{self.name}, {self.start_date}, {self.end_date}'

    def __list__(self):
        return [self.name, self.start_date, self.end_date]

from typing import Any
from .custom_type import Score
from pydantic.types import PositiveInt
from pydantic import BaseModel


class Match(BaseModel):
    '''
        Class qui permet de créer un match entre deux joueurs
        et donner le résultat final du match.
    '''
    player_1_id: PositiveInt
    player_2_id: PositiveInt
    player_1_score: Score = None

    def __str__(self):
        return f'{self.player_1_id}, {self.player_1_id}, {Score(self.player_1_score).name}'

    def __list__(self):
        return [self.player_1_id, self.player_2_id, Score(self.player_1_score).name]

    @property
    def player_2_score(self):
        return Score(1.0 - self.player_1_score).value if self.player_1_score is not None\
            else None

    @player_2_score.setter
    def player_2_score(self, value: float):
        if isinstance(value, float):
            if self.player_1_score:
                self.player_1_score = Score(1.0 - value)

    def __eq__(self, other: Any) -> bool:
        return min(self.player_1_id, self.player_2_id) == min(other.player_1_id, other.player_2_id) and\
            max(self.player_1_id, self.player_2_id) == max(other.player_1_id, other.player_2_id)

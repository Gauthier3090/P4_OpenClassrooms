from .score import Score
from pydantic.types import PositiveInt
from pydantic import BaseModel


class Match(BaseModel):
    player_1_id: PositiveInt
    player_2_id: PositiveInt
    player_1_score: Score = None

    def __str__(self):
        return f'{self.player_1_id}, {self.player_2_id}, {self.player_1_score.name}\
            , {self.player_2_score.name}'

    @property
    def player_2_score(self):
        return Score(1.0 - self.player_1_score.value) if self.player_1_score\
            else None

    @player_2_score.setter
    def player_2_score(self, value: float):
        if isinstance(value, float):
            if self.player_1_score:
                self.player_1_score = Score(1.0 - value)

from datetime import datetime
from pydantic.main import BaseModel
from pydantic.types import PositiveInt, constr
from typing import List
from models.round import Round
from models.timecontrol import TimeControl
from models.match import Match
from models.score import Score
from views import Menu
from player_manager import pm
from tournament_manager import tm


class Tournament(BaseModel):
    id: PositiveInt
    name: constr(min_length=5, max_length=20)
    location: constr(min_length=5, max_length=20)
    start_date: datetime = datetime.today()
    end_date: datetime = None
    number_of_rounds: PositiveInt = 4
    rounds: List[Round] = []
    players: List[PositiveInt] = []
    time_control: TimeControl
    description: constr(min_length=5, max_length=40)

    def __str__(self):
        return f'{self.id}: {self.name}, {self.location}, {self.start_date},\
            {self.end_date}, {self.time_control.name}, {self.description}'

    def sort_ranking_player(self):
        sort_player = []
        for player in self.players:
            if not sort_player:
                sort_player.append(player)
            else:
                data_player = pm.read(player)
                ranking = data_player['ranking']
                print(ranking)

    def generate_first_round(self):
        for player_1, player_2 in zip(self.players[:len(self.players) // 2],
                                      self.players[len(self.players) // 2:]):
            self.rounds.append(Round(name='Premier round',
                                     matches=[Match(player_1_id=player_1,
                                                    player_2_id=player_2)]))

    def generate_next_round(self):
        for round in self.rounds:
            for match in round.matches:
                if match.player_1_score == Score.WIN.value:
                    self.players.remove(match.player_2_id)
                elif match.player_1_score == Score.LOOSE.value:
                    self.players.remove(match.player_1_id)
        for player_1, player_2 in zip(self.players[:len(self.players) // 2],
                                      self.players[len(self.players) // 2:]):
            self.rounds.append(Round(name='Prochain round',
                                     matches=[Match(player_1_id=player_1,
                                                    player_2_id=player_2)]))

    def play(self, menu: Menu):
        if len(self.players) > 1:
            if not self.rounds:
                self.generate_first_round()
            for round in self.rounds:
                if not round.end_date:
                    for match in round.matches:
                        match.player_1_score = Score(float(menu.display())).value
                    round.end_date = datetime.today()
            self.generate_next_round()
            if len(self.players) == 1:
                self.end_date = datetime.today()
            tm.save_item(self.id)

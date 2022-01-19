from datetime import datetime
from pydantic.main import BaseModel
from pydantic.types import PositiveInt, constr
from typing import List
from models.round import Round
from models.match import Match
from models.custom_type import Score, TimeControl
from views import Menu
from player_manager import pm


class Tournament(BaseModel):
    '''
        Class qui instancie un tournoi et qui prends en parametre
        differents informations comme le nombre de joueurs et de rounds.
    '''
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

    def __list__(self):
        return [self.id, self.name, self.location, self.start_date, self.end_date,
                self.time_control.name, self.description]

    def __info__(self):
        return self.name

    def sort_ranking_first_round(self):
        list_player = []
        sort_player = []
        for player in self.players:
            list_player.append((player, pm.read(player).ranking))
        list_player = sorted(list_player, key=lambda tup: tup[1], reverse=True)
        for player in list_player:
            sort_player.append(player[0])
        return sort_player

    def sort_ranking_next_round(self):
        sort_player = []
        for player in self.players:
            previous_opposant = []
            score = 0.0
            for round in self.rounds:
                for match in round.matches:
                    if player == match.player_1_id:
                        score += match.player_1_score
                        previous_opposant.append(match.player_2_id)
                    if player == match.player_2_id:
                        score += match.player_2_score
                        previous_opposant.append(match.player_1_id)
            sort_player.append((player, score, pm.read(
                player).ranking, previous_opposant))
        return sort_player

    def generate_first_round(self, index: int):
        sort_player = sorted(self.players, key=lambda id: pm.read(id).ranking, reverse=True)
        for player_1, player_2 in zip(sort_player[:len(sort_player) // 2],
                                      sort_player[len(sort_player) // 2:]):
            self.rounds.append(Round(name=f'Round {index}',
                                     matches=[Match(player_1_id=player_1,
                                                    player_2_id=player_2)]))
            index += 1
        return index

    @property
    def matchs(self):
        for round in self.rounds:
            for match in round.matches:
                yield match

    def get_player_score(self, id: int):
        score = 0.0
        for round in self.rounds:
            for match in round.matches:
                if id == match.player_1_id:
                    score += match.player_1_score
                if id == match.player_2_id:
                    score += match.player_2_score
        return score

    def generate_next_round(self, index: int):
        sort_player = sorted(self.players, key=lambda id:
                             (-self.get_player_score(id)))
        while sort_player:
            p1 = sort_player.pop(0)
            for p2 in sort_player:
                match = Match(player_1_id=p1, player_2_id=p2)
                if match not in self.matchs or len(sort_player) == 1:
                    sort_player.pop(sort_player.index(p2))
                    self.rounds.append(Round(name=f'Round {index}', matches=[match]))
                    index += 1
                    break
            else:
                p2 = sort_player.pop(0)
        return index

    def play(self, menu: Menu, tm):
        if not self.end_date:
            index = 1
            for i in range(0, self.number_of_rounds):
                if not self.rounds:
                    index = self.generate_first_round(index)
                for round in self.rounds:
                    if not round.end_date:
                        for match in round.matches:
                            match.player_1_score = Score(
                                float(menu.display())).value
                        round.end_date = datetime.today()
                if i != self.number_of_rounds - 1:
                    index = self.generate_next_round(index)
                else:
                    self.end_date = datetime.today()
                tm.save_item(self.id)

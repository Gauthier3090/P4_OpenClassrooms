from typing import List
from pydantic import BaseModel
from datetime import datetime, date
from pydantic.class_validators import validator
from pydantic.types import PositiveInt, constr
from enum import Enum


class Gender(Enum):
    Male = 'M'
    Female = 'F'
    NonBinary = 'X'


class Name(str):
    def __new__(cls, value):
        if not value.isalpha():
            raise ValueError('must contain only letters of the alphabet')
        if len(value) > 20:
            raise ValueError('is too long (Max 20 caracters)')
        return str.__new__(cls, value)


class Player(BaseModel):
    firstname: Name
    lastname: Name
    birthdate: date
    gender: Gender
    ranking: PositiveInt
    id: PositiveInt

    @validator("birthdate")
    def check_age(cls, birthdate: date):
        today = date.today()
        if birthdate.month > today.month:
            age = today.year - birthdate.year - 1
        else:
            age = today.year - birthdate.year
        if age < 12:
            raise ValueError('Your age is too small')
        return birthdate

    def __str__(self):
        return f'{self.id}, {self.firstname}, {self.lastname}, {self.birthdate}\
        , {self.gender.name}, {self.ranking}'


class Score(Enum):
    WIN = 1.0
    LOOSE = 0.0
    DRAW = 0.5


class Match(BaseModel):
    player_1_id: PositiveInt
    player_2_id: PositiveInt
    player_1_score: Score = None
    player_2_score: Score = None

    def __str__(self):
        return f'{self.player_1_id}, {self.player_2_id}, {self.player_1_score.name}\
            , {self.player_2_score.name}'


class Round(BaseModel):
    name = constr(min_length=5, max_length=20)
    matches: List[Match] = []
    start_date: datetime
    end_date: datetime = None

    def __str__(self):
        return f'{self.name}, {self.matches.__str__()}, {self.start_date}\
            , {self.end_date}'


class TimeControl(Enum):
    BULLET = 'bullet'
    BLITZ = 'blitz'
    COUP_RAPIDE = 'coup rapide'


class Tournament(BaseModel):
    id: PositiveInt
    name: constr(min_length=5, max_length=20)
    location: constr(min_length=5, max_length=20)
    start_date: datetime
    end_date: datetime = None
    number_of_rounds: PositiveInt = 4
    rounds: List[Round] = []
    players: List[PositiveInt] = []
    time_control: TimeControl
    description: constr(min_length=5, max_length=40)

    def __str__(self):
        return f'{self.id}: {self.name}, {self.location}, {self.start_date},\
            {self.end_date}, {self.time_control.name}, {self.description}'

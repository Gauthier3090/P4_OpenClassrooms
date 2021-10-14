from typing import List
from pydantic import BaseModel
from datetime import datetime, date
from pydantic.class_validators import validator
from pydantic.types import PositiveInt, constr
from enum import Enum


class Gender(Enum):
    Male = 'H'
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


class Match:
    player_1: tuple(Player, int)
    player_2: tuple(Player, int)
    result: constr(min_length=5, max_length=20)


class Round:
    rounds: List[Match] = []
    start_date: datetime
    end_date: datetime = None


class TimeControl(Enum):
    bullet = 'bullet'
    blitz = 'blitz'
    coup_rapide = 'coup_rapide'


class Tournament:
    name: constr(min_length=5, max_length=20)
    location: constr(min_length=5, max_length=20)
    start_date: datetime
    end_date: datetime = None
    rounds: List[Round] = []
    players: List[PositiveInt] = []
    time_control: TimeControl
    description: constr(min_length=5, max_length=40)
    id: PositiveInt

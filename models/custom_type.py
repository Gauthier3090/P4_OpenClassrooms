from enum import Enum


class Gender(Enum):
    Male = 'M'
    Female = 'F'
    NonBinary = 'X'


class Score(Enum):
    WIN = 1.0
    LOOSE = 0.0
    DRAW = 0.5


class TimeControl(Enum):
    BULLET = 'bullet'
    BLITZ = 'blitz'
    COUP_RAPIDE = 'coup rapide'


class Name(str):
    def __new__(cls, value):
        if not value:
            raise ValueError('Vous avez rentré une valeur vide')
        if not all(v.isalpha() or v.isspace() for v in value):
            raise ValueError('Votre nom doit seulement contenir des lettres de l\'alphabet')
        if len(value) > 20:
            raise ValueError('Vous avez rentré une valeur trop longue (Maximum 20 caractères)')
        return str.__new__(cls, value)


class NameTournament(Name):
    def __new__(cls, value):
        if len(value) < 5:
            raise ValueError('Vous avez rentré une valeur trop petite (Minimum 5 caractères)')
        return super().__new__(cls, value)


class Year(int):
    def __new__(cls, value):
        value = int(value)
        if value < 1940 or value > 2010:
            raise ValueError('L\'année doit être comprise entre 1940..2010 !')
        return int.__new__(cls, value)


class Month(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


class Day(int):
    def __new__(cls, value):
        value = int(value)
        if value < 1 or value > 31:
            raise ValueError('Le jour doit être comprise entre 1..31 !')
        return int.__new__(cls, value)


class NumberPlayer(int):
    def __new__(cls, value):
        value = int(value)
        if value % 2 != 0:
            raise ValueError('Le nombre de joueurs doit être pair')
        return int.__new__(cls, value)


class NumberRound(int):
    def __new__(cls, value, max_player):
        value = int(value)
        if value > int(max_player) - 1:
            raise ValueError('Le nombre de tours surpassent le nombre autorisé')
        return int.__new__(cls, value)

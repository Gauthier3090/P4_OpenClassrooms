from pydantic import BaseModel
from datetime import date
from pydantic.class_validators import validator
from pydantic.types import PositiveInt
from .custom_type import Name, Gender


class Player(BaseModel):
    '''
        Class Player qui permet d'instancier un joueur
        elle prend en parametre les differents informations
        d'un joueur comme son rang.
    '''
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
            raise ValueError('Vous êtes trop jeune.')
        return birthdate

    def __str__(self):
        return f'{self.id}, {self.firstname}, {self.lastname}, {self.birthdate}\
        , {self.gender.name}, {self.ranking}'

    def __list__(self):
        return [self.firstname, self.lastname, self.birthdate, self.gender.name, self.ranking]

    def __info__(self):
        return f'{self.lastname} {self.firstname}'

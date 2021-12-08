from pydantic import BaseModel
from datetime import date
from pydantic.class_validators import validator
from pydantic.types import PositiveInt
from .name import Name
from .gender import Gender


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

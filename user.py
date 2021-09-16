from pydantic import BaseModel
from datetime import datetime
from pydantic.class_validators import validator
from pydantic.types import PositiveInt

class User(BaseModel):
    '''Create an user in the datebase'''

    firstname: str
    lastname: str
    birthday: str
    gender: str
    ranking: PositiveInt

    @validator('firstname')
    def check_firstname(cls, firstname: str):
        if not firstname.isalpha():
            raise ValueError('must contain only letters of the alphabet')
        if len(firstname) > 20:
            raise ValueError('is too long (Max 20 caracters)')
        return firstname
    
    @validator('lastname')
    def check_lastname(cls, lastname: str):
        if not lastname.isalpha():
            raise ValueError('must contain only letters of the alphabet')
        if len(lastname) > 20:
            raise ValueError('is too long (Max 20 caracters)')
        return lastname
    
    @validator("birthday")
    def check_birthday(cls, birthday: str):
        try:
            birth = datetime.strptime(birthday, "%d/%m/%Y")
            return birth.date()
        except ValueError:
            raise ValueError("Incorrect data format, should be DD/MM/YYYY")
    
    @validator("birthday")
    def check_age(cls, birthday: datetime):
        today = datetime.today()
        if birthday.month > today.month:
            age = today.year - birthday.year - 1
        else:
            age = today.year - birthday.year
        if age < 12:
            raise ValueError('Your age is too small')
        return birthday

    @validator("gender")
    def check_gender(cls, gender: str):
        if (gender == 'Male' or gender == 'Female' or gender == 'X'):
            return gender
        else:
            raise ValueError("Invalid gender")
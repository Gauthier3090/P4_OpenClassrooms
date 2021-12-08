class Name(str):
    def __new__(cls, value):
        if not value.isalpha():
            raise ValueError('must contain only letters of the alphabet')
        if len(value) > 20:
            raise ValueError('is too long (Max 20 caracters)')
        return str.__new__(cls, value)

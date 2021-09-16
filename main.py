from datetime import date
from user import User

if __name__ == "__main__":
    user = User(firstname='Gauthier', lastname='Pladet', birthday='06/11/1996', gender='Male', ranking=1)
    print(user.birthday)
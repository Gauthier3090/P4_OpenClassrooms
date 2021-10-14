from player import Player, Name
from views import Menu, Form

if __name__ == "__main__":
    form = Form('Create a player', 'Form to create a player', dict(p1='firstname', p2='lastname', p3='rank', p4='gender', p5='birthdate'))
    data = form.get_input()
    player = Player(firstname=Name(data['firstname']), lastname=Name(data['lastname']), birthdate=data['birthdate'], gender=data['gender'], ranking=data['rank'])

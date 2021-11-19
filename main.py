from controllers import list_player_by_name_controller, list_player_controller, list_tournament_controller, main_menu_controller, player_menu_controller, tournament_menu_controller
from models import Player, Name
from views import ListView, MainMenu, Menu, Form
from managers import player_manager as pm, tournament_manager as tm
from router import router

if __name__ == "__main__":
    #form = Form('Create a player', 'Form to create a player', dict(p1='firstname', p2='lastname', p3='rank', p4='gender', p5='birthdate'))
    #data = form.get_input()
    #player = Player(firstname=Name(data['firstname']), lastname=Name(data['lastname']), birthdate=data['birthdate'], gender=data['gender'], ranking=data['rank'])
    #Objectifs: appliquer la class router et refaire les menus
    #Developper la fonction main pour avoir differents enchainements avec le menu
    router.add_route('/', main_menu_controller)
    router.add_route('/players', player_menu_controller)
    router.add_route('/tournaments', tournament_menu_controller)
    router.add_route('/tournaments/play', player_menu_controller)
    router.add_route('/tournaments/list', list_tournament_controller)
    router.add_route('/players/list', list_player_controller)
    router.add_route('/players/list/order-by-name', list_player_by_name_controller)
    router.navigate('/')
    #ListView('List of players', pm.read_all()).display()
    #ListView('List of tournaments', tm.read_all()).display()
from controllers import main_menu_controller
from models import Player, Name
from views import ListView, MainMenu, Menu, Form
from managers import player_manager as pm, tournament_manager as tm

if __name__ == "__main__":
    #form = Form('Create a player', 'Form to create a player', dict(p1='firstname', p2='lastname', p3='rank', p4='gender', p5='birthdate'))
    #data = form.get_input()
    #player = Player(firstname=Name(data['firstname']), lastname=Name(data['lastname']), birthdate=data['birthdate'], gender=data['gender'], ranking=data['rank'])
    #Objectifs: Bien separer les vues et les controllers, faire en sorte que les menus renvois des str explicites, essayer de sauvegarder un joueur et un tournoi dans le fichier .json
    #Developper la fonction main pour avoir differents enchainements avec le menu
    main_menu_controller()
    #ListView('List of players', pm.read_all()).display()
    #ListView('List of tournaments', tm.read_all()).display()
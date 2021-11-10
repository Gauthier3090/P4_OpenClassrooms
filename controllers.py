from views import MainMenu, PlayerMenu


def main_menu_controller():
    input_user = MainMenu().display()
    if input_user == 'Joueurs':
        player_menu_controller()
    elif input_user == 'Tournois':
        TournamentMenu().display()
    elif input_user == 'Quitter':
        quit()

def player_menu_controller():
    input_user = PlayerMenu().display()
    if input_user == 1:
        ListPlayer().display()
    if input_user == 2:
        AddPlayerForm().display()
    if input_user == 3:
        ModifyPlayerForm().display()
    if input_user == 4:
        main_menu_controller()
    self.display()
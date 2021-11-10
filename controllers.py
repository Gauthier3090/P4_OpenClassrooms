from manager import Manager
from models import Player
from views import AddPlayerForm, AddTournamentForm, ListPlayer, ListTournament, ListView, MainMenu, ModifyPlayerForm, PlayMenu, PlayerMenu, TournamentMenu


def main_menu_controller():
    input_user = MainMenu().display()
    input_user = input_user[0]
    if input_user == 'Joueurs':
        player_menu_controller()
    elif input_user == 'Tournois':
        tournament_menu_controller()
    elif input_user == 'Quitter':
        quit()

def player_menu_controller():
    input_user = PlayerMenu().display()
    input_user = input_user[0]
    if input_user == 'Lister':
        list_player_controller()
    if input_user == 'Creer':
        add_player_controller()
    if input_user == 'Modifier':
        modify_player_controller()
    if input_user == 'Retour':
        main_menu_controller()

def tournament_menu_controller():
    input_user = TournamentMenu().display()
    input_user = input_user[0]
    if input_user == 'Lister':
        list_tournament_controller()
    if input_user == 'Creer':
        add_tournament_controller()
    if input_user == 'Jouer':
        play_menu_controller()
    if input_user == 'Retour':
        main_menu_controller()

def play_menu_controller():
    input_user = PlayMenu().display()
    input_user = input_user[0]
    if input_user == 'Lancer un tournoi':
        pass
    if input_user == 'Voir tournees':
        pass
    if input_user == 'Retour':
        tournament_menu_controller()

def add_tournament_controller():
    AddTournamentForm().display()
    tournament_menu_controller()


def list_tournament_controller():
    ListTournament().display()
    tournament_menu_controller()


def add_player_controller():
    AddPlayerForm().display()
    player_menu_controller()


def modify_player_controller():
    ModifyPlayerForm().display()
    player_menu_controller()


def list_player_controller():
    input_user = ListPlayer().display()
    input_user = input_user[0]
    pm = Manager(Player)
    all_players = pm.read_all()
    if input_user == 'Tous les joueurs par ordre alphabetique':
        all_players = sorted(all_players, key=lambda player: player.firstname)
        ListView('List des joueurs par ordre alphabetique', all_players).display()
    if input_user == 'Tous les joueurs par classement':
        all_players = sorted(all_players, key=lambda player: player.ranking, reverse=True)
        ListView('Tous les joueurs par classement', all_players).display()
    if input_user == 'Retour':
        player_menu_controller()
    list_player_controller()
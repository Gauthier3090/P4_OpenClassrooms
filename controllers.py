from manager import Manager
from player_manager import pm
from models import Player
from router import Router, router
from views import AddPlayerForm, AddTournamentForm, ListPlayer, ListTournament, ListView, MainMenu, ModifyPlayerForm, PlayMenu, PlayerMenu, TournamentMenu


def main_menu_controller():
    router.navigate(MainMenu().display())

def player_menu_controller():
    router.navigate(PlayerMenu().display())

def tournament_menu_controller():
    router.navigate(TournamentMenu().display())

def play_menu_controller():
    router.navigate(PlayerMenu().display())

def add_tournament_controller():
    AddTournamentForm().display()
    #Ajouter un tournoi fichier .json
    router.navigate('/tournaments')

def list_tournament_controller():
    router.navigate(ListTournament().display())

def add_player_controller():
    data = AddPlayerForm().display()
    pm.save(data)
    router.navigate('/players')

def modify_player_controller():
    ModifyPlayerForm().display()
    #Modifier le contenu dans le fichier .json
    router.navigate('/tournaments')

def list_player_controller():
    router.navigate(ListPlayer().display())

def list_player_by_name_controller():
    all_players = sorted(pm.read_all(), key=lambda player: player.firstname)
    ListView('List des joueurs par ordre alphabetique', all_players).display()
    router.navigate('/players')
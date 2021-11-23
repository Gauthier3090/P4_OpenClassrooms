from player_manager import pm
from router import router
from views import AddPlayerForm, AddTournamentForm, ListPlayer, ListTournament
from views import ListView, MainMenu, UpdatePlayerForm, PlayerMenu
from views import TournamentMenu


def main_menu_controller():
    router.navigate(MainMenu().display())


def player_menu_controller():
    router.navigate(PlayerMenu().display())


def tournament_menu_controller():
    router.navigate(TournamentMenu().display())


def play_menu_controller():
    router.navigate(PlayerMenu().display())


def add_tournament_controller():
    # Ajouter un tournoi fichier .json
    AddTournamentForm().display()
    router.navigate('/tournaments')


def list_tournament_controller():
    router.navigate(ListTournament().display())


def add_player_controller():
    data = AddPlayerForm().display()
    pm.create(**data)
    router.navigate('/players')


def update_player_controller():
    data = UpdatePlayerForm().display()
    pm.update_item(data['id'], int(data['new ranking']))
    router.navigate('/tournaments')


def list_player_controller():
    router.navigate(ListPlayer().display())


def list_player_by_name_controller():
    all_players = sorted(pm.read_all(), key=lambda player: player.firstname)
    ListView('List des joueurs par ordre alphabetique', all_players).display()
    router.navigate('/players')


def list_player_by_rank_controller():
    all_players = sorted(
        pm.read_all(), key=lambda player: player.ranking, reverse=True)
    ListView('List des joueurs par classement', all_players).display()
    router.navigate('/players')

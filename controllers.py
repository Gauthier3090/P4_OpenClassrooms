from player_manager import pm
from tournament_manager import tm
from router import router
from views import AddPlayerForm, AddTournamentForm, ListPlayer, Menu
from views import ListTournament, PlayMenu
from views import ListView, MainMenu, UpdatePlayerForm, PlayerMenu
from views import TournamentMenu


def main_menu_controller():
    router.navigate(MainMenu().display())


def player_menu_controller():
    router.navigate(PlayerMenu().display())


def tournament_menu_controller():
    router.navigate(TournamentMenu().display())


def launch_tournament_controller():
    id = input('ID du tournoi ? ')
    tournament = tm.read(int(id))
    tournament.play(Menu('Score du joueur 1', [('WIN', '1.0'),
                                               ('LOOSE', '0.0'),
                                               ('DRAW', '0.5')]), tm)


def play_menu_controller():
    router.navigate(PlayMenu().display())


def add_tournament_controller():
    data = AddTournamentForm().display()
    data['players'] = list(data['players'].split(' '))
    tm.create(**data)
    router.navigate('/tournaments')


def list_tournament_controller():
    router.navigate(ListTournament().display())


def add_player_controller():
    data = AddPlayerForm().display()
    pm.create(**data)
    router.navigate('/players')


def update_player_controller():
    data = UpdatePlayerForm().display()
    player = pm.read(data['id'])
    player.ranking = data['ranking']
    pm.save_item(player.id)
    router.navigate('/tournaments')


def list_player_controller():
    router.navigate(ListPlayer().display())


def list_player_by_name_controller():
    all_players = sorted(pm.read_all(), key=lambda player: player.firstname)
    ListView('Liste des joueurs par ordre alphabetique', all_players).display()
    router.navigate('/players')


def list_player_by_rank_controller():
    all_players = sorted(
        pm.read_all(), key=lambda player: player.ranking, reverse=True)
    ListView('Liste des joueurs par classement', all_players).display()
    router.navigate('/players')


def list_all_tournaments_controller():
    all_tournaments = sorted(
        tm.read_all(), key=lambda tournament: tournament.id)
    ListView('Liste de tous les tournois', all_tournaments).display()
    router.navigate('/tournaments')

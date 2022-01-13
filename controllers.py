from player_manager import pm
from tournament_manager import tm
from router import router
from views import AddPlayerForm, AddTournamentForm, ItemMenu, ListPlayer, Menu
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
    id = ItemMenu('Choisissez un tournoi', tm.read_all()).display()
    tournament = tm.read(id)
    tournament.play(Menu('Score du joueur 1', [('WIN', '1.0'),
                                               ('LOOSE', '0.0'),
                                               ('DRAW', '0.5')]), tm)
    router.navigate('/tournaments')


def play_menu_controller():
    router.navigate(PlayMenu().display())


def add_tournament_controller():
    data = AddTournamentForm().display()
    data['players'] = [ItemMenu('Choisissez les joueurs', pm.read_all(
    ), True).display() for _ in range(data['number_of_players'])]
    tm.create(**data)
    router.navigate('/tournaments')


def list_tournament_controller():
    router.navigate(ListTournament().display())


def list_all_rounds_controller():
    all_tournaments = []
    for id, tournament in enumerate(tm.read_all(), start=1):
        all_tournaments.append((tournament.name, id))
    id = Menu('Choisissez un tournoi', all_tournaments).display()
    headers = ['Date de début', 'Date de fin']
    ListView(headers, tm.read(id).rounds).display()
    router.navigate('/tournaments')


def list_all_matchs_controller():
    all_tournaments = []
    for id, tournament in enumerate(tm.read_all(), start=1):
        all_tournaments.append((tournament.name, id))
    id = Menu('Choisissez un tournoi', all_tournaments).display()
    all_match = []
    for round in tm.read(id).rounds:
        for matches in round:
            if matches[0] == 'matches':
                for match in matches[1]:
                    all_match.append(match)
    headers = ["ID du joueur 1", "ID du joueur 2", "Résultat du joueur 1"]
    ListView(headers, all_match).display()
    router.navigate('/tournaments')


def add_player_controller():
    data = AddPlayerForm().display()
    print(data)
    input()
    pm.create(**data)
    router.navigate('/players')


def update_player_controller():
    id = ItemMenu('Choix du joueur', pm.read_all()).display()
    data = UpdatePlayerForm().display()
    player = pm.read(id)
    player.ranking = data['ranking']
    pm.save_item(player.id)
    router.navigate('/players')


def list_player_controller():
    router.navigate(ListPlayer().display())


def list_player_by_name_controller():
    header = ['Prénom', 'Nom', 'Date de naissance', 'Sexe', 'Rang']
    all_players = sorted(pm.read_all(), key=lambda player: player.firstname)
    ListView(header, all_players).display()
    router.navigate('/players')


def list_player_by_rank_controller():
    header = ['Prénom', 'Nom', 'Date de naissance', 'Sexe', 'Rang']
    all_players = sorted(
        pm.read_all(), key=lambda player: player.ranking, reverse=True)
    ListView(header, all_players).display()
    router.navigate('/players')


def list_all_tournaments_controller():
    all_tournaments = sorted(
        tm.read_all(), key=lambda tournament: tournament.id)
    headers = ['ID', 'Nom du tournoi', 'Lieu', 'Date du début', 'Date de fin', 'Controle du temps', 'Description']
    ListView(headers, all_tournaments).display()
    router.navigate('/tournaments')

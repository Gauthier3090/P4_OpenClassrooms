from router import router
from controllers import (
    add_player_controller,
    launch_tournament_controller,
    list_all_rounds_win_controller,
    list_all_tournaments_controller,
    play_menu_controller,
    add_tournament_controller,
    update_player_controller,
    list_player_by_name_controller,
    list_player_by_rank_controller,
    list_player_controller,
    list_tournament_controller,
    main_menu_controller,
    player_menu_controller,
    tournament_menu_controller,
    list_all_rounds_controller,
    list_all_matchs_controller
)

if __name__ == "__main__":
    router.add_route('/', main_menu_controller)
    router.add_route('/players', player_menu_controller)
    router.add_route('/players/add', add_player_controller)
    router.add_route('/players/update', update_player_controller)
    router.add_route('/tournaments', tournament_menu_controller)
    router.add_route('/tournaments/play', play_menu_controller)
    router.add_route('/tournaments/play/launch', launch_tournament_controller)
    router.add_route('/tournaments/list', list_tournament_controller)
    router.add_route('/tournaments/list/all', list_all_tournaments_controller)
    router.add_route('/tournaments/list/rounds', list_all_rounds_controller)
    router.add_route('/tournaments/list/matchs', list_all_matchs_controller)
    router.add_route('/tournaments/list/win', list_all_rounds_win_controller)
    router.add_route('/tournaments/add', add_tournament_controller)
    router.add_route('/players/list', list_player_controller)
    router.add_route('/players/list/order-by-name',
                     list_player_by_name_controller)
    router.add_route('/players/list/order-by-rank',
                     list_player_by_rank_controller)
    router.navigate('/')


# Lister les vainqueurs d'un tournoi
# Le nombre de joueurs quand on cree un tournoi doit etre pair
# Maximum de tour = Max Joueur - 1
# Docstring
# readme
# powerpoint (contexte, rappel des librairies env, git, qualite du code, MVC, comment appliquer le MCV,3
# les difficultes rencontrées, manager, routeur, un ou deux algos, lancer flake8 et demo, axe d'amelioration)
# Ajouter requirements.txt

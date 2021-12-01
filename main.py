from router import router
from controllers import add_player_controller, launch_tournament_controller
from controllers import list_all_tournaments_controller, play_menu_controller
from controllers import add_tournament_controller
from controllers import update_player_controller
from controllers import list_player_by_name_controller
from controllers import list_player_by_rank_controller
from controllers import list_player_controller
from controllers import list_tournament_controller
from controllers import main_menu_controller
from controllers import player_menu_controller
from controllers import tournament_menu_controller

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
    router.add_route('/tournaments/add', add_tournament_controller)
    router.add_route('/players/list', list_player_controller)
    router.add_route('/players/list/order-by-name',
                     list_player_by_name_controller)
    router.add_route('/players/list/order-by-rank',
                     list_player_by_rank_controller)
    router.navigate('/')

from typing import Any, List, Tuple
from os import system, name


class View:
    def __init__(self, title: str, content: str, blocking: bool = False):
        self.title = title
        self.content = content
        self.blocking = blocking

    def display(self):
        system('cls' if name == 'nt' else 'clear')
        print(self.title)
        print('*' * len(self.title))
        print(self.content)
        if self.blocking:
            input()


class ListView(View):
    def __init__(self, title: str, items: List[Any]):
        content = '\n'.\
            join([str(item) for item in items])
        super().__init__(title, content, True)


class ErrorView(View):
    def __init__(self, error: str):
        super().__init__('Error', error, True)


class Menu(View):
    def __init__(self, title: str, options: List[Tuple[str, str]]):
        content = '\n'.\
            join([f"{nb}. {option}" for nb, (option, _)
                  in enumerate(options, start=1)])
        super().__init__(title, content)
        self.options = options

    def display(self):
        super().display()
        element = input()
        if element.isdigit():
            value = int(element)
            if not 0 < value <= len(self.options):
                return self.display()
            return self.options[value - 1][1]
        else:
            return self.display()


class Form(View):
    def __init__(self, title: str, fields: List[str]):
        content = '\n'.\
            join([f"{nb}. {val}" for nb, val in enumerate(fields, start=1)])
        super().__init__(title, content)
        self.fields = fields
        self.data = {}

    def display(self):
        for field in self.fields:
            self.data[field] = input(field + ' ? ')
        return self.data


class MainMenu(Menu):
    def __init__(self):
        title = 'Chess Maker V1.00'
        options = [('Joueurs', '/players'), ('Tournois', '/tournaments'),
                   ('Quitter', '/quit')]
        super().__init__(title, options)


class PlayerMenu(Menu):
    def __init__(self):
        title = 'Joueurs'
        options = [('Lister', '/players/list'), ('Ajouter', '/players/add'),
                   ('Modifier', '/players/update'), ('Retour', '/')]
        super().__init__(title, options)


class PlayMenu(Menu):
    def __init__(self):
        title = 'Jouer'
        options = [('Lancer un tournoi', '/tournaments/play/launch'),
                   ('Voir tournees', '/tournaments/play/list'),
                   ('Retour', '/tournaments')]
        super().__init__(title, options)


class TournamentMenu(Menu):
    def __init__(self):
        title = 'Tournois'
        options = [('Lister', '/tournaments/list'),
                   ('Creer', '/tournaments/add'),
                   ('Jouer', '/tournamements/play'), ('Retour', '/')]
        super().__init__(title, options)


class AddPlayerForm(Form):
    def __init__(self):
        title = 'Creer un joueur'
        fields = ['firstname', 'lastname', 'birthdate', 'gender', 'ranking']
        super().__init__(title, fields)


class UpdatePlayerForm(Form):
    def __init__(self):
        title = 'Modifier un joueur'
        fields = ['id', 'new ranking']
        super().__init__(title, fields)


class AddTournamentForm(Form):
    def __init__(self):
        title = 'Creer un tournoi'
        fields = ['Nom', 'Lieu', 'Date', 'Nombre de tours',
                  'Nombre de joueurs',
                  'Controle du temps', 'Description']
        super().__init__(title, fields)


class ListTournament(Menu):
    def __init__(self):
        title = 'Lister tournois'
        options = [('Tous les tournois', '/tournaments/list/all'),
                   ('Tous les tours d un tournoi', '/tournaments/list/rounds'),
                   ('Tous les matchs d un tournoi',
                   '/tournaments/list/matchs'),
                   ('Retour', '/tournaments')]
        super().__init__(title, options)


class ListPlayer(Menu):
    def __init__(self):
        title = 'Lister joueurs'
        options = [('Tous les joueurs par ordre alphabetique',
                    '/players/list/order-by-name'),
                   ('Tous les joueurs par classement',
                   '/players/list/order-by-rank'), ('Retour', '/players')]
        super().__init__(title, options)

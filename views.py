from enum import Enum
from typing import Any, Dict, List, Tuple, Type
from os import system, name
from datetime import date
from models.custom_type import Day, Gender, Month, Name, NameTournament, TimeControl, Year, NumberPlayer, NumberRound
from tabulate import tabulate


class View:
    def __init__(self, title: str, content: str = None, blocking: bool = False, clear: bool = True):
        self.title = title
        self.content = content
        self.blocking = blocking
        self.clear = clear

    def display(self):
        if self.clear:
            system('cls' if name == 'nt' else 'clear')
        if self.content:
            print(tabulate([[self.title], [self.content]],
                  tablefmt='fancy_grid'))
        if self.blocking:
            input()


class ListView():
    def __init__(self, title: List[str], items: List[Any]):
        self.title = title
        self.content = [item for item in items]

    def display(self):
        system('cls' if name == 'nt' else 'clear')
        input(tabulate(self.content, self.title, tablefmt="fancy_grid"))


class Menu(View):
    def __init__(self, title: str, options: List[Tuple[str, str]], clear: bool = True):
        content = '\n'. \
            join([f"{nb}. {option}" for nb, (option, _)
                  in enumerate(options, start=1)])
        super().__init__(title, content, False, clear)
        self.options = options

    def display(self):
        super().display()
        element = input('\nChoix du numéro: ')
        if element.isdigit():
            value = int(element)
            if not 0 < value <= len(self.options):
                return self.display()
            return self.options[value - 1][1]
        else:
            return self.display()


class Form(View):
    def __init__(self, title: str, fields: List[Tuple[str, str, Type]], clear: bool = True):
        super().__init__(title, None, False, clear)
        self.fields = fields
        self.template = Form.gen_template(fields)

    def init_list_models(self):
        models = {}
        for k in self.fields:
            models.setdefault(k[0])
        return models

    @staticmethod
    def gen_template(fields):
        return '\n'.join(f'{f[1]}: {{{f[0]}}}' for f in fields)

    def render_template(self, **params):
        self.content = self.template.format(
            **{k: (v if v is not None else "N/A") for k, v in params.items()}
        )

    def post_exec(self, data: Dict):
        return data

    def display(self):
        models = self.init_list_models()
        self.render_template(**models)
        super().display()
        for k, f in zip(models.keys(), self.fields):
            while True:
                try:
                    if issubclass(f[2], Enum):
                        v = EnumView('Choix possible', [
                                     v for v in f[2]]).display()
                    elif issubclass(f[2], NumberRound):
                        v = f[2](input('\n' + f[1] + ' ? '),
                                 models['number_of_players'])
                    else:
                        v = f[2](input('\n' + f[1] + ' ? '))
                    models[k] = v
                    self.render_template(**models)
                    super().display()
                    break
                except ValueError as e:
                    super().display()
                    print(f'\nErreur: {e} \n')
        return self.post_exec(models)


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
                   ('Tableau des scores d\'un tournoi', '/tournaments/play/list'),
                   ('Retour', '/tournaments')]
        super().__init__(title, options)


class TournamentMenu(Menu):
    def __init__(self):
        title = 'Tournois'
        options = [('Lister', '/tournaments/list'),
                   ('Creer', '/tournaments/add'),
                   ('Jouer', '/tournaments/play'), ('Retour', '/')]
        super().__init__(title, options)


class AddPlayerForm(Form):
    def __init__(self):
        title = 'Créer un joueur'
        fields = [('firstname', 'Prénom', Name),
                  ('lastname', 'Nom', Name),
                  ('year', 'Année', Year),
                  ('month', 'Mois', Month),
                  ('day', 'Jour', Day),
                  ('gender', 'Sexe', Gender),
                  ('ranking', 'Classement', int)]
        super().__init__(title, fields)

    def post_exec(self, data: Dict):
        data['birthdate'] = date(data['year'], data['month'], data['day'])
        return data


class UpdatePlayerForm(Form):
    def __init__(self):
        title = 'Modifier un joueur'
        fields = [('ranking', 'Classement', int)]
        super().__init__(title, fields)


class AddTournamentForm(Form):
    def __init__(self):
        title = 'Créer un tournoi'
        fields = [('name', 'Nom du tournoi', NameTournament),
                  ('location', 'Lieu du tournoi', NameTournament),
                  ('number_of_players', 'Nombre de joueurs', NumberPlayer),
                  ('number_of_rounds', 'Nombre de tours', NumberRound),
                  ('time_control', 'Controle du temps', TimeControl),
                  ('description', 'Description', NameTournament)]
        super().__init__(title, fields)


class ListTournament(Menu):
    def __init__(self):
        title = 'Lister tournois'
        options = [('Tous les tournois', '/tournaments/list/all'),
                   ('Tous les tours d un tournoi', '/tournaments/list/rounds'),
                   ('Tous les matchs d un tournoi',
                    '/tournaments/list/matchs'),
                   ('Tous les vainqueurs d un tournoi', '/tournaments/list/win'),
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


class ItemMenu(Menu):
    def __init__(self, title: str, items: List[Any], exit: bool = False):
        self.options = [(str(item.__info__()), item.id) for item in items]
        if exit:
            self.options.append(('Fin des choix', 'exit'))
        super().__init__(title, self.options)


class EnumView(Menu):
    def __init__(self, title: str, items: List[Any]):
        options = [(item.name, item.value) for item in items]
        super().__init__(title, options, False)

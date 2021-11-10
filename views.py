from typing import Any, List, Tuple
from os import system, name
from manager import Manager

from models import Player

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
            join([f"{nb}. {option}" for nb, (option, _) in enumerate(options, start=1)])
        super().__init__(title, content)
        self.options = options

    def display(self):
        super().display()
        element = input()
        if element.isdigit():
            value = int(element)
            if not 0 < value <= len(self.options):
                value = self.display()
            print(self.options[value - 1])
            return self.options[value - 1]
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
        options = [('Joueurs', 1), ('Tournois', 2), ('Quitter', 3)]
        super().__init__(title, options)
    
    def display(self):
        input_user = super().display()
        if input_user == 'Joueurs':
            PlayerMenu().display()
        elif input_user == 'Tournois':
            TournamentMenu().display()
        elif input_user == 'Quitter':
            quit()


class PlayerMenu(Menu):
    def __init__(self):
        title = 'Joueurs'
        options = ['Lister', 'Creer', 'Modifier', 'Retour']
        super().__init__(title, options)
    
    def display(self):
        input_user = super().display()
        if input_user == 1:
            ListPlayer().display()
        if input_user == 2:
            AddPlayerForm().display()
        if input_user == 3:
            ModifyPlayerForm().display()
        if input_user == 4:
            MainMenu().display()
        self.display()


class PlayMenu(Menu):
    def __init__(self):
        title = 'Jouer'
        options = ['Lancer un tournoi', 'Voir tournees', 'Retour']
        super().__init__(title, options)
    
    def display(self):
        input_user = super().display()
        if input_user == 1:
            pass
        if input_user == 2:
            pass
        if input_user == 3:
            pass


class TournamentMenu(Menu):
    def __init__(self):
        title = 'Tournois'
        options = ['Lister', 'Creer', 'Jouer', 'Retour']
        super().__init__(title, options)
    
    def display(self):
        input_user = super().display()
        if input_user == 1:
            ListTournament().display()
        if input_user == 2:
            AddTournamentForm().display()
        if input_user == 3:
            PlayMenu().display()
        if input_user == 4:
            MainMenu().display()
        self.display()


class AddPlayerForm(Form):
    def __init__(self):
        title = 'Creer un joueur'
        fields = ['Nom', 'Prenom', 'Rang', 'Sexe', 'Date de naissance']
        super().__init__(title, fields)

    def display(self):
        return super().display()


class ModifyPlayerForm(Form):
    def __init__(self):
        title = 'Modifier un joueur'
        fields = ['Rang']
        super().__init__(title, fields)

    def display(self):
        return super().display()


class AddTournamentForm(Form):
    def __init__(self):
        title = 'Creer un tournoi'
        fields = ['Nom', 'Lieu', 'Date', 'Nombre de tours', 'Nombre de joueurs', 'Controle du temps', 'Description']
        super().__init__(title, fields)
    
    def display(self):
        return super().display()


class ListTournament(Menu):
    def __init__(self):
        title = 'Lister tournois'
        options = ['Tous les tournois', 'Tous les tours d un tournoi', 'Tous les matchs d un tournoi', 'Retour']
        super().__init__(title, options)
    
    def display(self):
        return super().display()


class ListPlayer(Menu):
    def __init__(self):
        title = 'Lister joueurs'
        options = ['Tous les joueurs par ordre alphabetique', 'Tous les joueurs par classement', 'Retour']
        super().__init__(title, options)
    
    def display(self):
        input_user = super().display()
        pm = Manager(Player)
        all_players = pm.read_all()
        if input_user == 1:
            all_players = sorted(all_players, key=lambda player: player.firstname)
            ListView('List des joueurs par ordre alphabetique', all_players).display()
        if input_user == 2:
            all_players = sorted(all_players, key=lambda player: player.ranking, reverse=True)
            ListView('Tous les joueurs par classement', all_players).display()
        if input_user == 3:
            PlayerMenu().display()
        self.display()

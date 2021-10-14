from typing import List
from os import system, name


class View:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def display(self):
        system('cls' if name == 'nt' else 'clear')
        print(self.title)
        print('*' * len(self.title))
        print(self.content)


class Menu(View):
    def __init__(self, title: str, options: List[str]):
        content = '\n'.\
            join([f"{nb}. {val}" for nb, val in enumerate(options, start=1)])
        super().__init__(title, content)
        self.options = options

    def display(self):
        super().display()
        element = input()
        if element.isdigit():
            value = int(element)
            if not 1 < value <= len(self.options):
                value = self.display()
            return value
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


Menu('Chess Maker V1', ['Joueurs', 'Tournois', 'Jouer', 'Quitter'])
Menu('Joueurs', ['Lister', 'Creer', 'Modifier', 'Retour']).display()
Form('Creer un joueur', ['Nom', 'Prenom', 'Rang', 'Sexe', 'Date de naissance'])

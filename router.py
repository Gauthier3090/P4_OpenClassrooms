from typing import Any


class Router:
    '''
        But: Permet de naviguer et de créer les menus grace au chemin indiqué avec la
        méthode naviagate() et add_route()
    '''
    def __init__(self):
        self.routes = []

    def add_route(self, path: str, controller: Any):
        self.routes.append((path, controller))

    def navigate(self, path: str):
        for p, controller in self.routes:
            if p == path:
                controller()
                break


router = Router()

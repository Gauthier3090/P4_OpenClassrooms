from typing import Any


class Router:
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

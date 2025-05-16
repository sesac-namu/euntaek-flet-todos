import flet as ft


class Route:
    path: str
    view: ft.View

    def __init__(self, path: str, view_components: list[ft.Control]):
        self.path = path
        self.view = ft.View(path, view_components)


class Router:
    history: list[str]
    routes: list[Route]
    current_path: str
    page: ft.Page

    @classmethod
    def create(cls, page: ft.Page):
        return cls(page)

    def __init__(self, page: ft.Page):
        self.history = []
        self.routes = []
        self.current_path = page.route
        self.page = page

    def add_route(self, path: str, view_components: list[ft.Control]):
        route = Route(path, view_components)
        self.routes.append(route)

    def navigate(self, path: str, append_history: bool = True):
        for route in self.routes:
            if route.path == path:
                self.page.views.clear()
                self.page.views.append(route.view)
                self.page.update()

                if append_history:
                    self.history.append(path)
                return

        raise ValueError(f"Route {path} not found")

    def go_back(self):
        if len(self.history) > 1:
            self.navigate(self.history[-2], append_history=False)
            self.history.pop()

    def go_forward(self):
        if len(self.history) > 0 and self.history[-1] != self.current_path:
            self.navigate(self.history[-1], append_history=False)
            self.history.pop()

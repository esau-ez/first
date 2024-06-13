import flet as ft
from splash import SplashScreen
from login import LoginScreen
from puntear import Puntear
from comprobar import Comprobar
class App:
    def __init__(self):
        self.page = None
        self.routes = {
            '/': SplashScreen,
            '/login': LoginScreen,
            "/puntear": Puntear,
            "/comprobar": Comprobar
        }
    def main(self, page: ft.Page):
        self.page = page
        self.page.title = "Aplicación con Flet"
        page.fonts={
            "Poppins":"assets/Fonts/Poppins/Poppins-Medium.ttf",
            "Poppins-SB":"assets/Fonts/Poppins/Poppins-SemiBold.ttf"
        }
        self.page.on_route_change = self.route_change
        self.route_to('/')

    def route_to(self, route: str):
        self.page.go(route)
    
    def route_change(self, e):
        screen_class = self.routes.get(e.route, None)
        if screen_class is None:
            screen = ft.Text("Página no encontrada")
        else:
            screen = screen_class(self)

        self.page.clean()
        self.page.add(screen)
        self.page.update()

app = App()
ft.app(target=app.main,assets_dir="assets")
